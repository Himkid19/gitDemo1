from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from blog2.models import UserProfile,monthly_pay,HouseInfo
from django.contrib.auth.models import User,Group
from datetime import datetime
from blog2.form import set_count

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


def setting_count_page(request,house_no):
    if request.method == 'POST':
        count_set = set_count(request.POST)
        if count_set.is_valid():
            water_rate = int(count_set.cleaned_data.get('water_rate'))
            power_rate = int(count_set.cleaned_data.get('power_rate'))
            house_rent = int(count_set.cleaned_data.get('house_rent'))
            else_rate = int(count_set.cleaned_data.get('else_rate'))
            remark = count_set.cleaned_data.get('remark')
            total = 0
            total = water_rate + power_rate + house_rent + else_rate
            print(total)
            count_dict = count_set.cleaned_data
            house_no_obj = HouseInfo.objects.get(house_no=house_no)
            try:
                monthly_pay.objects.create(**count_dict,house_no=house_no_obj,total=total)
                print('create success')
            except Exception as e:
                print(e)
            return redirect('/index/choice_payment/set_payment/house_no='+house_no)
    else:
        count_set = set_count()
    try:
        count_setting_record = monthly_pay.objects.filter(house_no=house_no)
    except Exception as e:
        print(e)
    return render(request,'set_payment_page.html',locals())

def delete_rate_record(request,id,house_no):
    monthly_pay.objects.filter(id=id).delete()
    return redirect('/index/choice_payment/set_payment/house_no='+house_no)

def Room_setting_page(request):
    house_gather = HouseInfo.objects.all()
    return render(request,'room_setting_page.html',locals())

def Edit_Info_page(request,house_no):

    return render(request,'owner page/edit_house_info.html',locals())
