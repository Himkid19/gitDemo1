from django.shortcuts import render,redirect,render_to_response
from blog2.form import RegisterForm,LoginForm,Re_set,forget_PW
from django.contrib.auth.models import User,Group
from blog2.models import UserProfile
from django.contrib import auth
from django.contrib.auth.hashers import check_password
from django.db import models
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
            user = auth.authenticate(username=username,password=password)

            if user and user.is_active :
                auth.login(request,user)
                return redirect('/index/')
            else:
                message = "password is wrong!"
                return render(request,'login.html',locals())
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

def reset_pw(request):

    if request.user.is_authenticated and request.method == "POST":
        set_pw = Re_set(request.POST)
        username = request.user.username
        password = request.user.password
        print(set_pw.errors)
        if set_pw.is_valid():
            old_password = set_pw.cleaned_data.get('old_password')

            if check_password(old_password,password)==True:
                user = auth.authenticate(username=username,password=old_password)
                newpassword = set_pw.cleaned_data.get('new_password2')
                user.set_password(newpassword)
                user.save()
                auth.logout(request)
                return redirect("/login/")
            else:
                message = "password is wrong"

    else:
        if request.user.is_authenticated == False and request.method == 'GET':
            return redirect("/login/")
    set_pw = Re_set()
    return render(request,"re_set_pw.html",locals())


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



