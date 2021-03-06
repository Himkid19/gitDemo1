from django.shortcuts import render,redirect,render_to_response,HttpResponse
from blog2.form import RegisterForm,LoginForm,Re_set,forget_PW
from django.contrib.auth.models import User,Group
from blog2.models import UserProfile
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from django.db import models
from dwebsocket import accept_websocket
from django.http import JsonResponse
import json
# Create your views here.
def register(request):
    if request.method == "POST":
        register = RegisterForm(request.POST)
        print(register.errors)
        if register.is_valid():
            username = register.cleaned_data.get('username')
            telephone = register.cleaned_data.get('telephone')
            password = register.cleaned_data.get('password')
            password2 = register.cleaned_data.get('password2')
            user = User.objects.create_user(username=username,password=password2)
            UserProfile.objects.create(user=user,telephone=telephone)
            user_profile = UserProfile(user=user,telephone = telephone)
            user_group = auth.authenticate(username=username,password=password2)
            group = Group.objects.get(name='游客')
            user_group.groups.add(group)

            #   another writer
            # group.user_set.add(user)
            return redirect('/login/')
    else:
        register = RegisterForm()
    return render(request,'Register.html',locals())

def login(request):
    if request.user.is_authenticated:
        return redirect("/index/")
    if request.method == 'POST':
        login = LoginForm(request.POST)

        if login.is_valid():
            username = login.cleaned_data.get('username')
            password = login.cleaned_data.get('password')
            exist_user=User.objects.get(username=username)

            if exist_user:
                user = auth.authenticate(username=username, password=password)

                if user and user.is_active:
                    auth.login(request, user)
                    return redirect('/index/')
                else:
                    message = "password is wrong!"
                    print(message)
                    return render(request, 'login.html', locals())
            else:
                message = "User not exist!"
                print(message)
                return render(request, 'login.html', locals())


    else:
        login = LoginForm()

    return render(request,"login.html",locals())



def index(request):
    if request.user.is_authenticated:


        return render(request,'index.html')
    else:
        return redirect("/login/")
    return render(request,'index.html')

def log_out(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("/index/")


def forget_password(request):
    if request.method == "GET":
        forget_password = forget_PW()
        return render(request, 'forget_pw.html', locals())
    if request.method == "POST":
        forget_password = forget_PW(request.POST)
        print(forget_password.errors)
        if forget_password.is_valid():
            username = forget_password.cleaned_data.get('username')
            old_password = forget_password.cleaned_data.get('oldpassword')
            new_password = forget_password.cleaned_data.get('newpassword2')
            filter_result = User.objects.get(username=username).password
            if check_password(old_password,filter_result)==True:
                user = auth.authenticate(username=username,password=old_password)
                user.set_password(new_password)
                user.save()
                return redirect('/login/')
            else:
                message = "old password is wrong"
        return render(request, 'forget_pw.html', locals())



def chat_page(request):
    username = request.user.username
    return render(request,'chat-page.html',locals())

clients = {}
all_user_list = []
cur_user_list = {}
import uuid
@accept_websocket
def chat(request):
    username = request.user.username
    all_user = User.objects.all()
    # 所以用户
    if request.is_websocket():
        userid = str(uuid.uuid1())[::8]   #替换为userid
        # clients[userid] = request.websocket
        clients[userid] = request.websocket
        cur_user_list[username] = username
#         每一个websocket链接视为一个用户
        for i in all_user:
            ever_user_name = i.username
            all_user_list.append(ever_user_name)

        while True:
            for i in clients:
                print(i)
            msg = request.websocket.wait()
            if not msg:
                break
            else:
                msg = str(msg,encoding="utf-8")
                if msg == "test":
                    print("websocket conntect success"+userid)
                    # 当前在线用户
                    clients[userid].send(json.dumps({"type":"0","userid":userid,"cur_username":username,"cur_list":list(clients.keys()),"all_list":all_user_list,"cur_user_list":list(cur_user_list.keys())}))
                    all_user_list.clear()
                    # for client in clients:
                    #     # 所有用户列表
                    #     clients[client].send(json.dumps({"user":None,"type":"0","userlist":list(clients.keys())}))

#         删除离开聊天框的用户
        if userid in clients:
            del clients[userid]
            print(username+"离线")
            if username in cur_user_list:
                del cur_user_list[username]
                for client in clients:
                    clients[client].send(json.dumps({"user":None,"type":"0","cur_list":list(clients.keys()),"all_list":all_user_list,"cur_user_list":list(cur_user_list.keys())}).encode("'utf-8'"))


def send(request):
    msg = request.POST.get('txt')
    userto = request.POST.get('userto')
    userfrom = request.POST.get('userfrom')
    type = request.POST.get('type')
    #  返回json中 user为空即群发；user为userid即私发;type为1表示发送信息
    if type == '1':
    #群发
        for client in clients:
            clients[client].send(json.dumps({"type":"1","data":{"msg":msg,"user":userfrom}}).encode("'utf-8'"))
    else:
    #私发(匹配useridto在clients中),对方显示
        clients[userto].send(json.dumps({"type":"1","data":{"msg":msg,"user":userfrom}}).encode("'utf-8'"))
        #私发，自己显示
        clients[userfrom].send(json.dumps({"type":"1","data":{"msg":msg,"user":userfrom}}).encode("'utf-8'"))

    return HttpResponse(json.dumps({"msg":"success"}))

def normal_edit(request):
    try:
        user_obj = UserProfile.objects.get(user__username=request.user.username)
    except:
        print('this user not have info ')


    return render(request,'normal_edit_page.html',locals())

def re_set_pw(request):
    username = request.POST.get('username')
    oldpw = request.POST.get('oldpw')
    newpw = request.POST.get('newpw')
    filter_result = User.objects.get(username=username).password
    if check_password(oldpw,filter_result) == True:
        user = auth.authenticate(username=username, password=oldpw)
        user.set_password(newpw)
        user.save()
        return JsonResponse({'error_msg':'','type':'1'})
    else:
        return JsonResponse({'error_msg':'password is not match','type':'0'})

def edit_personal(request):
    phone_no = request.POST.get('phone_no')
    username = request.POST.get('username')
    print(username)
    try:
        filter_phone = UserProfile.objects.get(user__username=username).telephone
        if filter_phone == phone_no:
            return JsonResponse({'type':'0','error_msg':'手机号相同，请重新输入'})
        else:
            UserProfile.objects.filter(user__username=username).update(telephone=phone_no)
            return JsonResponse({'type':'1','error_msg':''})
    except Exception as e:
        print(e)
        return JsonResponse({'type':'0','error_msg':'找不到用户，系统异常'},content_type="application/json,charset=utf-8")

def test_jmeter(request):
    a=request.POST.get('a')
    b=request.POST.get('b')
    print(a,b)
    if request.method == 'GET':
        return JsonResponse({'code':'1','msg':'fail'})
    else:
        return JsonResponse({'code':'0','msg':'success','sum':a+b},content_type="application/json,charset=utf-8")

