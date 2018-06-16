# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import ConsultingCompany,MiningUnit


@admin.register(ConsultingCompany)
class ConsultingCompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(MiningUnit)
class MiningUnitAdmin(admin.ModelAdmin):
    pass
