# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
import os
from time import gmtime, strftime

from django.db import models


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4()).replace('-', ''), ext)
    path = strftime("evaluation/%Y/%m/%d", gmtime())
    return os.path.join(path, filename)


class Agent(models.Model):
    name = models.CharField(
        max_length=100
    )

    def __unicode__(self):
        return self.name


class Norma(models.Model):
    description = models.TextField()
    is_active = models.BooleanField(
        default=True
    )

    def __unicode__(self):
        return self.description


class Category(models.Model):
    norma = models.ForeignKey(
        Norma,
        related_name='norma_category'
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

    def __unicode__(self):
        return '%s - %s' % (self.description, self.norma)


class AgentCategory(models.Model):
    agent = models.ForeignKey(
        Agent,
        related_name='agent_agent_category'
    )
    category = models.ForeignKey(
        Category,
        related_name='category_agent_category'
    )

    def __unicode__(self):
        return '%s - %s' % (self.agent, self.category)


class ChainCustody(models.Model):
    user = models.ForeignKey(
        'customer.UserConsulting',
        related_name='user_chain_custody'
    )
    contributor_name = models.CharField(
        max_length=150
    )
    contributor_last_name = models.CharField(
        max_length=120
    )
    job_position = models.CharField(
        max_length=150
    )
    detail_project = models.ForeignKey(
        'project.DetailProject',
        related_name='project_chain_custody'
    )
    area = models.CharField(
        max_length=100
    )
    agent = models.ForeignKey(
        Agent,
        related_name='agent_chain_custody'
    )
    instrument = models.ForeignKey(
        'material.Instrument',
        related_name='instrument_chain_custody'
    )
    date_evaluation = models.DateField()
    description_activity = models.TextField()
    start_hour = models.IntegerField()
    end_hour = models.IntegerField()
    is_office_work = models.BooleanField(default=True)

    def __unicode__(self):
        return '%s - %s' % (self.contributor_name, self.date_evaluation)


class MeasurementValue(models.Model):
    chain_custody = models.ForeignKey(
        ChainCustody,
        related_name='chain_custody_measurement_value'
    )
    max = models.IntegerField()
    min = models.IntegerField()
    avg = models.IntegerField()
    point_reference = models.CharField(
        max_length=100
    )
    observation_measurement = models.TextField()
    type_lighting = models.CharField(
        max_length=250
    )

    def __unicode__(self):
        return '%s - %s' % (self.max, self.min)


class ReferentialImage(models.Model):
    measurement_value = models.ForeignKey(
        MeasurementValue,
        related_name='measurement_value_referential_image'
    )
    image = models.FileField(upload_to=get_file_path)
    longitude = models.CharField(
        null=True,
        max_length=20
    )
    latitude = models.CharField(
        null=True,
        max_length=20
    )
