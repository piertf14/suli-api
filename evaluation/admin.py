# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Agent, Norma, Category, AgentCategory, ChainCustody, MeasurementValue, ReferentialImage


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Norma)
class NormaAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_active')
    search_fields = ('description', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('norma', 'description', 'limit_description', 'limit_value', )
    search_fields = ('norma__description', 'description', )


@admin.register(AgentCategory)
class AgentCategoryAdmin(admin.ModelAdmin):
    list_display = ('agent', 'category', )
    search_fields = ('agent__name', 'category__description', )


@admin.register(ChainCustody)
class ChainCustodyAdmin(admin.ModelAdmin):
    list_display = ('user', 'detail_project', 'agent',)
    search_fields = ('user__name',)


@admin.register(MeasurementValue)
class MeasurementValueAdmin(admin.ModelAdmin):
    list_display = ('chain_custody', 'max', 'min', 'point_reference', )


@admin.register(ReferentialImage)
class ReferentialImageAdmin(admin.ModelAdmin):
    list_display = ('measurement_value', 'longitude', 'latitude')