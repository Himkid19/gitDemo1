from django.shortcuts import render,redirect,HttpResponse
from blog2.models import HouseInfo,monthly_pay,UserProfile
from django.contrib.auth.models import User,Group

def display_house_list(request):
    house_list = HouseInfo.objects.all()

    return render(request,'house_msg_list.html',locals())

def house_detail(request,id):
    detail = HouseInfo.objects.get(id=id)
    return render(request,"house_detail.html",locals())

def Check_account(request):
    pass

def my_paying_for(request):
    try:
        house_obj = HouseInfo.objects.get(user__username=request.user.username)
        try:
            payment_check = monthly_pay.objects.get(house_no=house_obj)
            print(payment_check.total)
        except Exception as e:
            payment_check = None
    except Exception as e:
        msg = '未安排房屋信息，请联系房主'
    return render(request,'rental_payment_page.html',locals())