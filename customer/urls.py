# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import MyUserAPI

urls_patterns = [
    url(r'^me/$', MyUserAPI.as_view(), name='me'),
]