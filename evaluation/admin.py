# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Agent, Norma, Category, AgentCategory, ChainCustody,\
    ContributorEvaluated, MeasurementValue, ReferentialImage


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    pass


@admin.register(Norma)
class NormaAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(AgentCategory)
class AgentCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ChainCustody)
class ChainCustodyAdmin(admin.ModelAdmin):
    pass


@admin.register(ContributorEvaluated)
class ContributorEvaluatedAdmin(admin.ModelAdmin):
    pass


@admin.register(MeasurementValue)
class MeasurementValueAdmin(admin.ModelAdmin):
    pass


@admin.register(ReferentialImage)
class ReferentialImageAdmin(admin.ModelAdmin):
    pass