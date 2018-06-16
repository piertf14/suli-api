# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Instrument, InstrumentCertificate


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    pass


@admin.register(InstrumentCertificate)
class InstrumentCertificateAdmin(admin.ModelAdmin):
    pass
