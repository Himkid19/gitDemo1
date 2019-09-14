from django.shortcuts import render,redirect,HttpResponse
from blog.models import *


# Create your views here.
def Register(request):

    if request.method == "GET":

        return render(request,"Register.html")
    if request.method == "POST":

        username = request.POST.get("login_user_name")
        PW = request.POST.get("login_Pw")
        PW2 = request.POST.get("login_Pw2")
        phone = request.POST.get("phone_No")

        if username and PW and phone:

            # username check
            try:
                is_username = User_Info.objects.filter(login_user_name = username)
            except Exception as e:
                is_username = None
            if is_username:
                user_err = 'this user already exist!'
                return render(request, "Register.html", locals())
            # different password check

            if PW != PW2:
                pw_err = "the second PW is different!"
                return render(request,"Register.html",locals())
            # check phone_no
            try:
                is_phone = User_Info.objects.filter(phone_No = phone)
            except Exception as e:
                is_phonee = None
            if is_phone:
                user_err = 'this phone already exist!'
                return render(request, "Register.html", locals())

            # # create User
            else:
                User_Info.objects.create(login_user_name = username,login_Pw = PW,phone_No = phone)
                print("create success",username)
            return redirect("/login/")
        else:
            user_err = 'username can not be None!'
            PW_err = 'PW can not be None!'
            phone_err = 'phone can not be None!'
            return render(request,"Register.html",locals())


def login(request):

    if request.method == 'GET':
        Login = login_check()
        User_list = User_Info.objects.all()
        return render(request, "login.html", locals())
    if request.method == 'POST':
        Login = login_check(request.POST)
        if Login.is_valid():
            username = Login.cleaned_data.get('Username')
            PW = Login.cleaned_data.get('PW')

            try:
                is_username = User_Info.objects.filter(login_user_name = username)
            except Exception as e:
                is_username = None
            if is_username:
                try:
                    is_PW = User_Info.objects.filter(login_user_name = username,login_Pw = PW)
                except Exception as e:
                    is_pW = None
                if is_PW:
                    return HttpResponse('Welcome')
                else:
                    PW_msg = 'PW is wrong'
                    return render(request,'login.html',locals())
            else:
                user_emsg = 'this user is not exist '

                return render(request,'login.html',locals())

def test_ret(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username,password)
    if username=='123'and password=="456":
        request.session['is_login'] = True
        request.session['username'] = username
        return redirect("/index.html/")
    else:
        err_msg = "error"
        return render(request,"TEST.html",locals())

def index(request):
    print(request.session.get('is_login'))
    if request.session.get('is_login') == True:
        master = request.session.get('username')
    else:
        master = "游客"
    return render(request,"index.html",locals())


