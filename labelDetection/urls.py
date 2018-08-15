# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:04:39 2018

@author: kmy07
"""

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.homepage),
    url(r'^upload/$', views.upload, name="upload"),
    url(r'^upload/detectLabels/$',views.detect_labels),
]