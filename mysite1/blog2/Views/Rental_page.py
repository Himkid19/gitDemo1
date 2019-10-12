from django.shortcuts import render,redirect,HttpResponse
from blog2.models import HouseInfo
from django.contrib.auth.models import User,Group

def display_house_list(request):
    house_list = HouseInfo.objects.all()

    return render(request,'house_msg_list.html',locals())

def house_detail(request,id):
    detail = HouseInfo.objects.get(id=id)
    return render(request,"house_detail.html",locals())
def Check_account(request):
    pass
def Check_Monthly_Rental(request):
    pass
