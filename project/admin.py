# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import StatusProject, Project, DetailProject


@admin.register(StatusProject)
class StatusProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(DetailProject)
class DetailProjectAdmin(admin.ModelAdmin):
    pass