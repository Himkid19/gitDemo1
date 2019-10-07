"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog2.Views import views,Rental_page,owner_page
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('login/', views.login),
    path('log_out/', views.log_out),
    path('index/reset_pw/', views.reset_pw),
    path('forget_pw/', views.forget_password),
    path('index/', views.index),
    path('index/house_list', Rental_page.display_house_list),
    path('index/waiting_list',owner_page.Waiting_Audit_Info),
    url(r'^index/waiting_list/audit_pass/(\d+)/$', owner_page.Audit_tenant_Info,name='audit_pass'),
    url(r'^index/house_list/detail/(\d+)/$', Rental_page.house_detail,name = 'detail'),


    url(r'^captcha', include('captcha.urls')),

]
