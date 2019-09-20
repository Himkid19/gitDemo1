from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=60,label="Username",required=True,error_messages={'required':'this is required'})

    telephone = forms.CharField(max_length=30,required=True,label="Telephone",error_messages={'required':'this is required'})
    password = forms.CharField(max_length=50,label="Password",required=True,widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50,label="Second Password",required=True,widget=forms.PasswordInput)

    def clean_username(self):
        usename = self.cleaned_data.get("username")
        fiter_result = User.objects.filter(username__exact = usename)
        if fiter_result:
            raise forms.ValidationError("this user is already exist ")
        return usename





    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password and password != password2:
            raise forms.ValidationError("password is not match, please reinput again!")
        return password2


