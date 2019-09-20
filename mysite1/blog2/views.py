from django.shortcuts import render,redirect
from .form import RegisterForm
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.
def register(request):
    if request.method == "POST":
        register = RegisterForm(request.POST)
        if register.is_valid():
            username = register.cleaned_data.get('username')
            telephone = register.cleaned_data.get('telephone')
            password = register.cleaned_data.get('password')
            password2 = register.cleaned_data.get('password2')
            print(password,password2)

            user = User.objects.create_user(username=username,password=password2)
            user_profile = UserProfile(user=user,telephone = telephone)
        return redirect('/login/')
    else:
        register = RegisterForm()
    return render(request,'Register.html',locals())

def login(request):
    user_list = UserProfile.objects.all()
    return render(request,"login.html",locals())
def index():
    pass
def log_out():
    pass
def reset_pw():
    pass