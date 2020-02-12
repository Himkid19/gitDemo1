from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.contrib.auth.hashers import check_password

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

class LoginForm(forms.Form):
    username = forms.CharField(max_length=60,label="Username",required=True,error_messages={'required':'this is required'},widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'name': 'text1',
                                                             'id': 'text1',
                                                             }))
    password = forms.CharField(max_length=50,label="Password",required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password','name': 'password','id': 'myInput', }))
    # captcha = CaptchaField(label='验证码')



    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(username__exact = username)
        if not filter_result:
            raise forms.ValidationError("this username is not exist ")
        return username


class Re_set(forms.Form):

    telephone = forms.CharField(max_length=60,label="Telephone",required=False)
    Code = forms.CharField(max_length=6,label="Code",required=False)
    oldpassword = forms.CharField(max_length=30,label="Old password",widget=forms.PasswordInput)
    newpassword1 = forms.CharField(max_length=30,label="New password",widget=forms.PasswordInput)
    newpassword2 = forms.CharField(max_length=30,label="Second password",widget=forms.PasswordInput)

    # def clean(self):
    #     oldpassword = self.cleaned_data.get('oldpassword')
    #     newpassword1 = self.cleaned_data.get('newpassword1')
    #     newpassword2 = self.cleaned_data.get('newpassword2')
    #     if oldpassword == newpassword1:
    #         self.add_error('newpassword1','can not be same')
    #     if newpassword1 != oldpassword:
    #         self.add_error('newpassword2','password is not match')
    #     return self.cleaned_data
    def clean_newpassword1(self):
        oldpassword = self.cleaned_data.get('oldpassword')
        newpassword1 = self.cleaned_data.get('newpassword1')
        if oldpassword == newpassword1:
            raise forms.ValidationError('new password can not be same ')
        return newpassword1



class forget_PW(forms.Form):
    username = forms.CharField(max_length=60, label="Username")
    telephone = forms.CharField(max_length=60, label="Telephone", required=False)
    Code = forms.CharField(max_length=6, label="Code", required=False)
    old_password = forms.CharField(max_length=30, label="Old password", widget=forms.PasswordInput)
    new_password1 = forms.CharField(max_length=30, label="New password", widget=forms.PasswordInput)
    new_password2 = forms.CharField(max_length=30, label="Second password", widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(username__exact = username)
        if not filter_result:
            raise forms.ValidationError("this username is not exist ")
        return username

    def clean_old_password(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username):
            old_password = self.cleaned_data.get('old_password')
            hash_password = User.objects.get(username=username).password
            if check_password(old_password,hash_password) == False :
                raise forms.ValidationError('password is wrong')
        return old_password

    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        if old_password == new_password1:
            raise forms.ValidationError('can not be same')
        return new_password1

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        if new_password1 != new_password2:
            raise forms.ValidationError('not match')
        return new_password2


class set_count(forms.Form):
    water_rate = forms.CharField(label='水费',max_length=30,widget=forms.NumberInput(attrs={'class':'form-control','id':'set-count-form','placeholder':'please input your water rate'}))
    power_rate = forms.CharField(label='电费',max_length=30,widget=forms.NumberInput(attrs={'class':'form-control','id':'set-count-form','placeholder':'please input your power rate'}))
    house_rent = forms.CharField(label='房费',max_length=32,widget=forms.NumberInput(attrs={'class':'form-control','id':'set-count-form','placeholder':'please input your house rent'}))
    else_rate = forms.CharField(label='其他费用',max_length=32,widget=forms.NumberInput(attrs={'class':'form-control','id':'set-count-form','placeholder':'please input your else rate'}))
    remark = forms.CharField(label='备注其他费用',max_length=32,widget=forms.Textarea(attrs={'class':'form-control','id':'else-form','placeholder':'please input your remark'}))

