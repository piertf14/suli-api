# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import InstrumentAPI

urls_patterns = [
    url(r'^instrument/$', InstrumentAPI.as_view(), name='instrument'),
]