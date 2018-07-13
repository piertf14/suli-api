# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import AgentAPI, CustodyChainAPI, MeasurementValueAPI, ReferentialImageAPI

urls_patterns = [
    url(r'^agent/$', AgentAPI.as_view(), name='agent'),
    url(r'^custody-chain/$', CustodyChainAPI.as_view(), name='custody_chain'),
    url(r'^measurement-value/$', MeasurementValueAPI.as_view(), name='measurement_value'),
    url(r'^referential-image/$', ReferentialImageAPI.as_view(), name='referential_image'),
]