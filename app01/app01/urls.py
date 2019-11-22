"""app01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from blog.views import login_2,test_ws

from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login.html/', login_2.login),
    path('Register.html/',login_2.Register ),
    path('index.html/',login_2.index),
    path('test.html/',login_2.test),
    path('log_out/',login_2.log_out),

    url(r'^captcha', include('captcha.urls')),
    path('to_sendmsg/',test_ws.to_sendmsg),
    path('to_recmsg/',test_ws.to_recmsg),
    path('link/',test_ws.link),
    path('send/',test_ws.send),
    path('ws_temp/',test_ws.ws_temp),
    path('echo_once/',test_ws.echo_once),
    path('to_chat/',test_ws.to_chat),
    path('chat/',test_ws.chat),
    path('msg_send/',test_ws.msg_send),

    path('chat_page/',login_2.chat_page),
    path('chat_set/',login_2.chat_set),


]
