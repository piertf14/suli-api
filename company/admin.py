# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import ConsultingCompany,MiningUnit


@admin.register(ConsultingCompany)
class ConsultingCompanyAdmin(admin.ModelAdmin):
    list_display = ('number_ruc', 'name', 'email', 'contact', 'position_name',)
    search_fields = ('number_ruc', )


@admin.register(MiningUnit)
class MiningUnitAdmin(admin.ModelAdmin):
    list_display = ('customer', 'name', )
    search_fields = ('customer__name', 'name')
