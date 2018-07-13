# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import ListProjectsAPI

urls_patterns = [
    url(r'^project/$', ListProjectsAPI.as_view(), name='projects'),
]