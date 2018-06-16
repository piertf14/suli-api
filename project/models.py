# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class StatusProject(models.Model):
    description = models.CharField(
        max_length=100
    )


class Project(models.Model):
    consulting_company = models.ForeignKey(
        'company.ConsultingCompany'
    )
    customer = models.ForeignKey(
        'customer.Customer'
    )
    observations = models.TextField()
    start_date = models.DateField(
        null=True,
        blank=True
    )
    end_date = models.DateField(
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        StatusProject,
        null=True
    )


class DetailProject(models.Model):
    project = models.ForeignKey(
        Project
    )
    mining_init = models.ForeignKey(
        'company.MiningUnit'
    )
    agent_category = models.ForeignKey(
        'evaluation.AgentCategory'
    )
    quantity = models.PositiveIntegerField()
    code_area = models.CharField(
        max_length=20
    )
    area = models.CharField(
        max_length=60
    )
