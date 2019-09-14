from django import forms
from captcha.fields import CaptchaField

class Register(forms.Form):
    Username = forms.CharField(max_length=60,required=True,label="username",widget=forms.TextInput(attrs={'class': 'form-control'}))
    PW = forms.CharField(max_length=60,widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="password")
    PW2 = forms.CharField(max_length=60,widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="Second password")
    phone = forms.CharField(max_length=60,widget=forms.TextInput(attrs={'class': 'form-control'}),label="phone")

class login_check(forms.Form):
    Username = forms.CharField(max_length=60,required=True)
    PW = forms.CharField(max_length=60,required=True,widget=forms.PasswordInput)
    random_code = CaptchaField(label="验证码")