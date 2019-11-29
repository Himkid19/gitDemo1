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
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index/waiting_list',owner_page.Waiting_Audit_Info),
    path('index/choice_payment',owner_page.choice_count),
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('login/', views.login),
    path('log_out/', views.log_out),
    path('forget_pw/', views.forget_password),
    path('index/',views.index),
    url(r'^captcha', include('captcha.urls')),
    path('index/house_list', Rental_page.display_house_list),
    path('index/my_payment', Rental_page.my_paying_for),
    url(r'^index/house_list/detail/(\d+)/$', Rental_page.house_detail,name = 'detail'),
    url(r'^index/choice_payment/set_payment/house_no=(?P<house_no>\d+)', owner_page.setting_count_page,
        name='set_payment'),
    url(r'^index/choice_payment/set_payment/del_record/id=(?P<id>\d+)&house_no=(?P<house_no>\d+)',
        owner_page.delete_rate_record, name='del_record'),
    url(r'^index/waiting_list/audit_pass/(\d+)/$', owner_page.Audit_tenant_Info, name='audit_pass'),
    url(r'^index/waiting_list/del/(\d+)/$', owner_page.del_rental_Info, name='del'),
    path('index/room_setting', owner_page.Room_setting_page),
    url(r'^index/room_setting/edit_info_page/house_no=(?P<house_no>\d+)',owner_page.Edit_Info_page,name='edit_info'),
    url(r'^index/room_setting/change_user/house_no=(?P<house_no>\d+)',owner_page.change_house_owner,name='change_user'),
    path('index/chat_page/',views.chat_page),
    path('chat/',views.chat),
    path('send/',views.send),
    url(r'^index/may_payment/pay_detail=(?P<pay_id>\d+)',Rental_page.payment_detail,name='payment_detail'),
    url(r'^index/may_payment/payment_info_to_set/order_id=(?P<order_id>\d+)&total=(?P<total>\d+)',Rental_page.alipay_page,name='sumbit_order'),
    path('index/normal_edit/',views.normal_edit),
    path('re_setpw/',views.re_set_pw),
    path('edit_personal/',views.edit_personal),
    path('index/room_setting/edit_info_page/update_hyd/',owner_page.update_hyd),
    path('index/room_setting/edit_info_page/update_MM/',owner_page.update_MM),
    url(r'^index/waiting_list/user_info/username=(?P<id>\d+)',owner_page.check_people_info,name='check_user'),
    path('index/my_apply',Rental_page.my_apply),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


