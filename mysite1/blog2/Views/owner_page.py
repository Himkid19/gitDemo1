from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from blog2.models import UserProfile,monthly_pay,HouseInfo,hydropower,Application_list
from django.contrib.auth.models import User,Group
from datetime import datetime
from blog2.form import set_count
from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

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
    try:
        water = hydropower.objects.get(house_no=house_no).water
        power = hydropower.objects.get(house_no=house_no).power
    except:
        water = ''
        power = ''
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
                monthly_pay.objects.create(**count_dict,house_no=house_no_obj,total=total,payment_status='0')
                print('create success')
            except Exception as e:
                print(e)
                print('error')
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
    cur_status = HouseInfo.objects.get(house_no=house_no).status
    if new_user == ' ':
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

# 审核申请页

def check_all_applicaion(request):
    apply_obj = Application_list.objects.all()
    for i in apply_obj:
        username = i.username
        user_obj = User.objects.get(username=username)
        try:
            house_no = HouseInfo.objects.get(user=user_obj).house_no
            try:
                payment_obj = monthly_pay.objects.filter(house_no=house_no)

            except Exception as e:
                print(e)
        except Exception as e:
            print(e)

    return render(request,'owner page/audit_application_page.html',locals())

def pass_audit(request,id):
    apply_obj = Application_list.objects.get(id=id)
    apply_type = apply_obj.type
    username = apply_obj.username
    user = User.objects.get(username=username)
    Application_list.objects.filter(id=id).update(status='1')
    if apply_type == '0':
        HouseInfo.objects.filter(user=user).update(user=None,status='0')
    return redirect('/index/audit_application/')

def no_pass_audit(request,id):
    apply_obj = Application_list.objects.get(id=id)
    Application_list.objects.filter(id=id).update(status='2')
    return redirect('/index/audit_application/')

def publich_info(request,house_no):
    for i in house_no:
        loucheng = i[0]
    try:
        driver = webdriver.Chrome()
        driver.get('https://gz.58.com/house.shtml')
        driver.find_element_by_xpath('//*[@id="commonTopbar_login"]/a[1]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/img').click()
        username_input = driver.find_element_by_xpath('//*[@id="username"]')
        username_input.clear()
        username_input.send_keys('15818183032')
        pw_input = driver.find_element_by_xpath('//*[@id="password"]')
        pw_input.clear()
        pw_input.send_keys('a419832308')
        driver.find_element_by_xpath('//*[@id="btn_account"]').click()
        driver.implicitly_wait(200)

        driver.find_element_by_xpath('//*[@id="fabu"]').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[1]/a').click()
        time.sleep(2)

        input_xiaoqu = driver.find_element_by_xpath('//*[@id="xiaoqu"]')

        input_xiaoqu.clear()
        input_xiaoqu.send_keys('横沙复建街住宅区')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="postForm"]/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li').click()

        time.sleep(2)

        input_si = driver.find_element_by_xpath('//*[@id="huxingshi"]')
        input_si.clear()
        input_si.send_keys('1')
        input_area = driver.find_element_by_xpath('//*[@id="area"]')
        input_area.clear()
        input_area.send_keys('30')
        input_float = driver.find_element_by_xpath('//*[@id="Floor"]')
        input_float.click()
        input_float.clear()
        input_float.send_keys(loucheng)

        input_louceng = driver.find_element_by_xpath('//*[@id="zonglouceng"]')
        input_louceng.clear()
        input_louceng.send_keys('7')
        select_dianti = driver.find_element_by_xpath('//*[@id="postForm"]/div[1]/div[2]/div[4]/div[1]/div[4]/div[1]')
        select_dianti.click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="postForm"]/div[1]/div[2]/div[4]/div[1]/div[4]/div[2]/ul/li[2]').click()
        time.sleep(2)
        input_cost = driver.find_element_by_xpath('//*[@id="MinPrice"]')
        input_cost.clear()
        input_cost.send_keys('300')
        driver.find_element_by_xpath('//*[@id="postForm"]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="postForm"]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/ul/li[2]').click()
        time.sleep(2)
        upload_file = driver.find_element_by_xpath('//*[@id="imgUpload"]/div/input')
        upload_file.click()
        time.sleep(2)
        upload_file.send_keys(r'D:\1211test.jpg')
        input_owner = driver.find_element_by_xpath('//*[@id="goblianxiren"]')
        input_owner.clear()
        input_owner.send_keys('陈')
        driver.find_element_by_xpath('//*[@id="postForm"]/div[5]/div[2]/div[1]/div[1]/div[3]/div[2]').click()
        time.sleep(600)
        while '稍后认证' in driver.page_source:
            msg='发布成功'
            driver.quit()
        return redirect('/index/room_setting')
    except:
        driver.close()
        msg='发布失败'
        return redirect('/index/room_setting')

# def publich_post(request):
#     house_no=request.POST.get('house_no')
#     print(house_no)
#     for i in house_no:
#         louceng=i[0]
#     print(louceng)
    # try:
    #     driver = webdriver.Chrome()
    #     driver.get('https://gz.58.com/house.shtml')
    #     driver.find_element_by_xpath('//*[@id="commonTopbar_login"]/a[1]').click()
    #     driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/img').click()
    #     username_input = driver.find_element_by_xpath('//*[@id="username"]')
    #     username_input.clear()
    #     username_input.send_keys('15818183032')
    #     pw_input = driver.find_element_by_xpath('//*[@id="password"]')
    #     pw_input.clear()
    #     pw_input.send_keys('a419832308')
    #     driver.find_element_by_xpath('//*[@id="btn_account"]').click()
    #     driver.implicitly_wait(200)
    #
    #     driver.find_element_by_xpath('//*[@id="fabu"]').click()
    #     driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[1]/a').click()
    #     time.sleep(2)
    #
    #     input_xiaoqu = driver.find_element_by_xpath('//*[@id="xiaoqu"]')
    #
    #     input_xiaoqu.clear()
    #     input_xiaoqu.send_keys('横沙复建街住宅区')
    #     time.sleep(2)
    #     driver.find_element_by_xpath('//*[@id="postForm"]/div[1]/div[2]/div[1]/div[1]/div[2]/div/ul/li').click()
    #
    #     time.sleep(2)
    #
    #     input_si = driver.find_element_by_xpath('//*[@id="huxingshi"]')
    #     input_si.clear()
    #     input_si.send_keys('1')
    #     input_area = driver.find_element_by_xpath('//*[@id="area"]')
    #     input_area.clear()
    #     input_area.send_keys('30')
    #     input_float = driver.find_element_by_xpath('//*[@id="Floor"]')
    #     input_float.click()
    #     input_float.clear()
    #     input_float.send_keys(louceng)
    #
    #     input_louceng = driver.find_element_by_xpath('//*[@id="zonglouceng"]')
    #     input_louceng.clear()
    #     input_louceng.send_keys('7')
    #     select_dianti = driver.find_element_by_xpath('//*[@id="postForm"]/div[1]/div[2]/div[4]/div[1]/div[4]/div[1]')
    #     select_dianti.click()
    #     time.sleep(2)
    #     driver.find_element_by_xpath('//*[@id="postForm"]/div[1]/div[2]/div[4]/div[1]/div[4]/div[2]/ul/li[2]').click()
    #     time.sleep(2)
    #     input_cost = driver.find_element_by_xpath('//*[@id="MinPrice"]')
    #     input_cost.clear()
    #     input_cost.send_keys('300')
    #     driver.find_element_by_xpath('//*[@id="postForm"]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]').click()
    #     time.sleep(2)
    #     driver.find_element_by_xpath('//*[@id="postForm"]/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/ul/li[2]').click()
    #     time.sleep(2)
    #     upload_file = driver.find_element_by_xpath('//*[@id="imgUpload"]/div/input')
    #     upload_file.click()
    #     time.sleep(2)
    #     upload_file.send_keys(r'D:\1211test.jpg')
    #     input_owner = driver.find_element_by_xpath('//*[@id="goblianxiren"]')
    #     input_owner.clear()
    #     input_owner.send_keys('陈')
    #     driver.find_element_by_xpath('//*[@id="postForm"]/div[5]/div[2]/div[1]/div[1]/div[3]/div[2]').click()
    #     time.sleep(600)
    #     while '稍后认证' in driver.page_source:
    #         return JsonResponse({'code':'1'})
    #     return JsonResponse({'code':'0'})
    # except:
    # return JsonResponse({'code':'2'})

