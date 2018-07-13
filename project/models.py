# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class StatusProject(models.Model):
    description = models.CharField(
        max_length=100
    )
    slug = models.CharField(
        max_length=100,
        null=True
    )

    def __unicode__(self):
        return self.description


class Project(models.Model):
    consulting_company = models.ForeignKey(
        'company.ConsultingCompany',
        related_name='consulting_company_project'
    )
    customer = models.ForeignKey(
        'customer.Customer',
        related_name='customer_project'
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

    def __unicode__(self):
        return '%s - %s' % (self.customer, self.consulting_company)


class DetailProject(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='project_detail_project'
    )
    mining_init = models.ForeignKey(
        'company.MiningUnit',
        related_name='mining_init_detail_project'
    )
    agent_category = models.ForeignKey(
        'evaluation.AgentCategory',
        related_name='agent_category_detail_project'
    )
    quantity = models.PositiveIntegerField()
    code_area = models.CharField(
        max_length=20
    )
    area = models.CharField(
        max_length=60
    )
