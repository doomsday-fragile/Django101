# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 00:39:19 2020

@author: Gaurav
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    ]

