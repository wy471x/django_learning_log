#!/usr/bin/env python
# coding=utf-8
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # login page
    url(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'),
    url(r'^logout/$', views.logout_view,
        name='logout'),

    url(r'^register/$', views.register, name='register'),
]
