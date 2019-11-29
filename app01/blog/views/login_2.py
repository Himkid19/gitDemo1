from django.shortcuts import render,redirect,HttpResponse
from blog import form
from blog.models import *
from dwebsocket import accept_websocket


def Register(request):
    if request.method == "GET":
        register = form.Register()
        return render(request,"Register.html",locals())
    elif request.method == "POST":
        register = form.Register(request.POST)

        if register.is_valid():
            username = register.cleaned_data["Username"]
            PW = register.cleaned_data["PW"]
            PW2 = register.cleaned_data["PW2"]
            phone = register.cleaned_data["phone"]
            ex_user = User_Info.objects.filter(login_user_name=username)
            ex_phone = User_Info.objects.filter(phone_No=phone)
            if ex_user:
                msg = "this username is exist!"
                return render(request,"Register.html",locals())
            elif ex_phone:
                msg = "this phone is exist!"
                return render(request,"Register.html",locals())
            elif PW!=PW2:
                msg = "there are different password,please input again!"
                return render(request,"Register.html",locals())
            else:
                User_Info.objects.create(login_user_name=username,
                                         login_Pw=PW,
                                         phone_No=phone,)
                return redirect("/login.html/")
        else:
            if register.is_valid()==None:
                msg = "message can't be empty!"
                return render(request,"Register.html",locals())
            else:
                return render(request,"Register.html")
def login(request):
    if request.method == "GET":
        login = form.login_check()
        exist_user_list = User_Info.objects.all()
        return render(request,"login.html",locals())
    if request.method == "POST":
        login = form.login_check(request.POST)
        if login.is_valid():
            username = login.cleaned_data["Username"]
            password = login.cleaned_data["PW"]
            is_username = User_Info.objects.filter(login_user_name=username)
            if is_username:
                is_username = User_Info.objects.get(login_user_name = username)
                is_PW = is_username.login_Pw
                print(is_PW)
                if is_PW == password:
                    request.session['is_login'] = True
                    request.session['id'] = is_username.id
                    request.session['username'] = username
                    return redirect("/index.html/")
                else:
                    msg ="password is wrong !"
                    return render(request,"login.html",locals())
            else:
                msg = "this username is not exist"
                return render(request,"login.html",locals())
        else:
            msg = "random code is wrong "
            return render(request,"login.html",locals())


def index(request):
    if request.session.get('is_login')==True:
        master = request.session.get('username')

        return render(request,"index.html",locals())
    else:
        master = "游客"
        return render(request,"index.html",locals())

def log_out(request):
    if request.session['is_login']:
        request.session.flush()
        return render(request,"index.html")
def test(requset):
    login = form.login_check()
    return render(requset,"TEST.html",locals())



def chat_page(request):
    user_list = User_Info.objects.all()
    return render(request,'chat_page.html',locals())


