# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserConsulting, Customer


@admin.register(UserConsulting)
class UserConsultingAdmin(admin.ModelAdmin):
    list_display = ('consulting_company', 'user', 'position', )
    search_fields = ('user__username', 'consulting_company__name', )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('consulting_company', 'number_ruc', 'name', 'number_telephone',)
    search_fields = ('consulting_company__name', 'name', )