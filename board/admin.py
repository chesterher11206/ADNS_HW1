from django.contrib import admin
from .models import Message, UserIP, VisitNumber

admin.site.register(Message)
admin.site.register(UserIP)
admin.site.register(VisitNumber)

# Register your models here.
