from django.shortcuts import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib import auth
from django.http import JsonResponse
from mysite1 import settings
from blog2.models import UserProfile,HouseInfo,Application_list,monthly_pay
import requests
import json
import uuid
def login(request):
    username = request.GET.get('username')
    password = request.GET.get('pw')
    code = request.GET.get('code')
    user_uuid = uuid.uuid4()
    try:
        user = User.objects.get(username=username)
    except Exception as e:
        user = None
        return JsonResponse({'code':'2','err_msg':'user not exist!'})
    if user:
        login_user = auth.authenticate(username=username,password=password)
        if login_user and login_user.is_active:
            APPID = settings.wx_APPID
            APPSECRET = settings.wx_APPSecret
            url = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code'.format(APPID, APPSECRET, code)
            r = requests.get(url)
            user_data = r.json()

            try:
                exitst_user = UserProfile.objects.get(openid=user_data['openid'])
                print(exitst_user)
                exitst_user.session_key=user_data['session_key']
                exitst_user.uuid=user_uuid
                exitst_user.save()

            except:
                first_user = UserProfile.objects.get(user__username=username)
                print(first_user)
                if first_user:
                    first_user.session_key=user_data['session_key']
                    first_user.uuid=user_uuid
                    first_user.save()
                else:
                    print('failed')
            return JsonResponse({'code':'1','err_msg':'','user':user_uuid})
        else:
            return JsonResponse({'code':'2','err_msg':'password is wrong'})


def index(request):
    uuid = request.GET.get('uuid')

    try:
        user = UserProfile.objects.get(uuid=uuid).user

        get_user = User.objects.get(username=user)
        group = get_user.groups.all()
        for i in group:
            user_group = i
        try:
            house_no = HouseInfo.objects.get(user__username=user)
            payment_list = monthly_pay.objects.filter(house_no=house_no)
        except Exception as e:
            payment_list = ''
            print(e)
            return JsonResponse({'user':str(user),'group':str(user_group)})
        all_payment = {}
        list=[]
        for i in payment_list:
            all_payment = {'total':i.total,'status_show':i.get_payment_status_display(),'create_time':i.create_time, 'status':i.payment_status }
            list.append(all_payment)

        return JsonResponse({'user':str(user),'group':str(user_group),'payment_list':list})
    except Exception as e:
        print(e)
    return JsonResponse({'user':str(user),'group':str(user_group)})

def my_application(request):
    type = request.GET.get('type')
    username = request.GET.get('username')
    content = request.GET.get('content')
    user_obj = User.objects.get(username=username)
    Application_list.objects.create(username=user_obj,type=type,content=content,status='0')

    return HttpResponse('OK')

def history_application(request):
    username = request.GET.get('username')

    try:
        apply_obj=Application_list.objects.filter(username=username)
        print(apply_obj)
        all_apply = {}
        apply_list = []
        for i in apply_obj:
            all_apply = {'type':i.get_type_display(),'content':i.content,'create_time':i.create_time,'status':i.get_status_display()}
            apply_list.append(all_apply)

        return JsonResponse({'code':'2','apply_list':apply_list})
    except:
        apply_obj=''
    return JsonResponse({'code':'1','apply_list':''})



