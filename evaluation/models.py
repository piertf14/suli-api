# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Agent(models.Model):
    name = models.CharField(
        max_length=100
    )


class Norma(models.Model):
    description = models.TextField()
    is_active = models.BooleanField(
        default=True
    )


class Category(models.Model):
    norma = models.ForeignKey(
        Norma
    )
    description = models.CharField(
        max_length=200
    )
    limit_description = models.CharField(
        max_length=250
    )
    limit_value = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


class AgentCategory(models.Model):
    agent = models.ForeignKey(
        Agent
    )
    category = models.ForeignKey(
        Category
    )


class ChainCustody(models.Model):
    user = models.ForeignKey(
        'customer.UserConsulting'
    )
    project = models.ForeignKey(
        'project.Project'
    )
    mining_unit = models.ForeignKey(
        'company.MiningUnit'
    )
    area = models.ForeignKey(
        'project.DetailProject'
    )
    agent = models.ForeignKey(
        Agent
    )
    instrument = models.ForeignKey(
        'material.Instrument'
    )

    date_evaluation = models.DateField()
    description_activity = models.TextField()
    instrument = models.ForeignKey(
        'material.Instrument'
    )
    start_hour = models.IntegerField()
    end_hour = models.IntegerField()
    is_office_work = models.BooleanField(default=True)


class ContributorEvaluated(models.Model):
    evaluation = models.ForeignKey(ChainCustody)
    contributor_name = models.CharField(
        max_length=150
    )
    contributor_last_name = models.CharField(
        max_length=120
    )
    job_position = models.CharField(
        max_length=150
    )


class MeasurementValue(models.Model):
    chain_custody = models.ForeignKey(
        ChainCustody
    )
    max = models.IntegerField()
    min = models.IntegerField()
    avg = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    point_reference = models.CharField(
        max_length=100
    )
    observation_measurement = models.TextField()
    type_lighting = models.CharField(
        max_length=250
    )


class ReferentialImage(models.Model):
    chain_custody = models.ForeignKey(
        ChainCustody
    )
    measurement_value = models.ForeignKey(
        MeasurementValue
    )
    image = models.FileField()
    longitude = models.IntegerField()
    latitude = models.IntegerField()
