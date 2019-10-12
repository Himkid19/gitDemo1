from django.shortcuts import render,redirect
from blog2.models import UserProfile,monthly_pay,HouseInfo
from django.contrib.auth.models import User,Group
from datetime import datetime

# 待审核列表
def Waiting_Audit_Info(request):
    v_Groups = Group.objects.get(name='游客')
    users = v_Groups.user_set.all()
    phone_list = []
    dict = {}
    for i in users:
        try:
            phone = UserProfile.objects.get(user__username=i.username).telephone
        except Exception as e:
            phone = "no number"
        dict = {'username':i.username,'phone_no':phone,'id':i.id}
        phone_list.append(dict)
    Groups_display = str(v_Groups)
    r_Groups = Group.objects.get(name='租客')
    r_users = r_Groups.user_set.all()
    r_display = str(r_Groups)
    return render(request,'waiting_audit_info.html',locals())

# 审核租客信息
def Audit_tenant_Info(request,id):
    group_rental = Group.objects.get(name='租客')
    group_normal = Group.objects.get(name='游客')
    user = User.objects.get(id=id)
    user.groups.remove(group_normal)
    user.groups.add(group_rental)
    return redirect('/index/waiting_list')

def del_rental_Info(request,id):
    user = User.objects.get(id=id)
    user.groups.clear()
    return redirect('/index/waiting_list')
def choice_count(request):
    house_list = HouseInfo.objects.all()

    return render(request,'choice_payment_page.html',locals())

def set_count(request,house_no):
    try:
        payment = monthly_pay.objects.get(house_no=house_no)
    except Exception as e:
        print(e)

    print(payment.create_time,payment.last_time)

    return render(request,'set_payment_page.html',locals())