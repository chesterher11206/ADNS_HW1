from .models import UserIP, VisitNumber
from .ipaddr import ip2addr


def visit_info(request, end_point):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
        ip = ip.split(",")[0]
    else:
        ip = request.META['REMOTE_ADDR']
    ip_exist = UserIP.objects.filter(ip=str(ip), end_point=end_point)

    if not "visit" in request.session:
        request.session["visit"] = True
        request.session.set_expiry(300)

        visit_num = VisitNumber.objects.all()
        if visit_num:
            visit_num = visit_num[0]
            visit_num.count += 1
        else:
            visit_num = VisitNumber()
            visit_num.count = 1
        visit_num.save()

        if ip_exist:
            user = ip_exist[0]
            user.count += 1
        else:
            user = UserIP()
            user.ip = ip
            user.end_point = end_point
            try:
                user.ip_addr = ip2addr(ip)
            except:
                user.ip_addr = 'unknown'
            user.count = 1
        user.save()
    return ip