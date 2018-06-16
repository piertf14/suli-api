# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import ListProjectsAPI

urls_patterns = [
    url(r'^company/(?P<pk>[0-9]+)/projects/$', ListProjectsAPI.as_view(), name='company-projects'),
]
