from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Message, UserIP, VisitNumber
from .forms import MessageForm
from .visit import visit_info

# Create your views here.
def board(request):
    ip = visit_info(request, '/')
    visit_num = VisitNumber.objects.all()[0].count
    user_num = len(UserIP.objects.all())
    user_index = 0
    for user in UserIP.objects.all().order_by('pk'):
        user_index += 1
        if ip == user.ip:
            break
    
    message_get = Message.objects.all()
    form = MessageForm()
    message_del = []
    for key in request.COOKIES.keys():
        if key.startswith("msg"):
            new_key = int(key.replace("msg", ""))
            msg_check = Message.objects.filter(pk=new_key).first()
            if msg_check:
                if msg_check.ip == ip and msg_check.text == request.COOKIES[key]:
                    message_del.append(new_key)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        print (request.POST)
        if form.is_valid():
            message_post = form.save(commit=False)
            message_post.ip = ip
            message_post.save()
            cookie_name = "msg{}".format(message_post.pk)
            cookie_value = message_post.text
            response = HttpResponseRedirect(reverse("board"))
            response.set_cookie(cookie_name, cookie_value)
            return response
        else:
            form = MessageForm()

    context = { "message_get": message_get,
                "message_del": message_del,
                "form": form,
                "visit_num": visit_num,
                "user_num": user_num,
                "user_index": user_index
    }
    return render(request, "board/post.html", context=context)

def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
        ip = ip.split(",")[0]
    else:
        ip = request.META['REMOTE_ADDR']
    msg_same = False
    for key in request.COOKIES.keys():
        if key.startswith("msg"):
            key_pk = int(key.replace("msg", ""))
            msg = request.COOKIES[key]
            if key_pk == pk and msg == message.text:
                msg_same = True
                break
    if ip == message.ip and msg_same:
        message.delete()
    return HttpResponseRedirect(reverse("board"))

@receiver(post_save, sender=VisitNumber)
def save_visitnum(sender, instance, **kwargs):
    print ("Signal")
