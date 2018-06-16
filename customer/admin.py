# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserConsulting, Customer


@admin.register(UserConsulting)
class UserConsultingAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass