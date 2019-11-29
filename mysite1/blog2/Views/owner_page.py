from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from blog2.models import UserProfile,monthly_pay,HouseInfo,hydropower
from django.contrib.auth.models import User,Group
from datetime import datetime
from blog2.form import set_count
from django.http import JsonResponse

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
    return render(request,'owner page/waiting_audit_info.html',locals())

# 审核租客信息
def Audit_tenant_Info(request,id):
    group_rental = Group.objects.get(name='租客')
    group_normal = Group.objects.get(name='游客')
    user = User.objects.get(id=id)
    user.groups.remove(group_normal)
    user.groups.add(group_rental)
    return redirect('/index/waiting_list')


def check_people_info(request,id):
    try:
        user_obj = UserProfile.objects.get(user__id=id)
    except:
        user_obj2 = User.objects.get(id=id)
        message = '未完善信息用户'
    return render(request,'owner page/check_user_info.html',locals())

def del_rental_Info(request,id):
    user = User.objects.get(id=id)
    user.groups.clear()
    return redirect('/index/waiting_list')



#########租金设置#################
def choice_count(request):
    house_list = HouseInfo.objects.all()
    return render(request,'owner page/choice_payment_page.html',locals())



def setting_count_page(request,house_no):
    status = HouseInfo.objects.get(house_no=house_no).status
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
    return render(request,'owner page/set_payment_page.html',locals())

def delete_rate_record(request,id,house_no):
    monthly_pay.objects.filter(id=id).delete()
    return redirect('/index/choice_payment/set_payment/house_no='+house_no)



############房屋信息设置#####################
def Room_setting_page(request):
    house_gather = HouseInfo.objects.all()
    return render(request,'owner page/room_setting_page.html',locals())

def Edit_Info_page(request,house_no):
    house_obj = HouseInfo.objects.get(house_no=house_no)
    print(house_obj.else_support)
    id = house_obj.id
    try:
        hydropower_obj = hydropower.objects.get(house_no=house_no)

    except Exception as e:
        hydropower_obj = ''
    try:
        current_user = house_obj.user.username
    except:
        current_user = ''
    group_rental = Group.objects.get(name='租客')
    r_users = group_rental.user_set.all()
    return render(request,'owner page/edit_house_info.html',locals())

def change_house_owner(request,house_no):
    new_user = request.POST.get('user-select')
    print(new_user)
    cur_status = HouseInfo.objects.get(house_no=house_no).status
    if new_user == 'null':
        HouseInfo.objects.filter(house_no=house_no).update(status='0',user=None)
        return redirect('/index/room_setting')

    try:
        user_obj = User.objects.get(username=new_user)
        HouseInfo.objects.filter(house_no=house_no).update(user=user_obj)
        if cur_status == '0':
            HouseInfo.objects.filter(house_no=house_no).update(status='1')
        return redirect('/index/room_setting')
    except Exception as e:
        msg = 'update failed'
        print('failed',e)
    return redirect('/index/room_setting/edit_info_page/house_no='+house_no)

def update_hyd(request):
    water = request.POST.get('water')
    power = request.POST.get('power')
    house_no = request.POST.get('house_no')

    try:
        hyd_obj = hydropower.objects.filter(house_no=house_no)
        hyd_obj.update(water=water, power=power)
        return JsonResponse({'type':'1','err_msg':''})
    except:
        return JsonResponse({'type':'0','err_msg':'系统异常'})

def update_MM(request):
    chair = request.POST.get('chair')
    table = request.POST.get('table')
    aircon = request.POST.get('aircon')
    blower = request.POST.get('blower')
    else_thing = request.POST.get('else_thing')
    house_no = request.POST.get('house_no')
    print(HouseInfo.objects.get(house_no=house_no).else_support)
    try:
        MM_obj = HouseInfo.objects.filter(house_no=house_no)

        MM_obj.update(chair=chair,
                      table=table,
                      aircon=aircon,
                      else_support=else_thing
                      )
        return JsonResponse({'type':'1','err_msg':''})
    except Exception as e:
        return JsonResponse({'type':'0','err_msg':e})
