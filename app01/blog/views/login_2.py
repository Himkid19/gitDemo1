from django.shortcuts import render,redirect
from blog import form
from blog.models import *


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
                return redirect("/login/")
        else:
            if register.is_valid()==None:
                msg = "message can't be empty!"
                return render(request,"Register.html",locals())
            else:
                return render(request,"Register.html")
def login(request):
    exist_user_list = User_Info.objects.all()
    return render(request,"login.html",locals())
def index(request):
    return render(request,"index.html")
def log_out(request):
    return render(request,"index.html")
