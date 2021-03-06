"""wxbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from django.urls import path,re_path,include
# from app01.views import *
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^app01/', include("app01.urls")),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^get_qrcode/', views.get_qrcode),
    url(r'^get_wx_id/', views.get_wx_id),
    url(r'^send/', views.send),
    url(r'^send_msg/', views.send_msg),
    url(r'^sweetajax/', views.sweetajax),
    url(r'^update/(\d+)$', views.update),
]
