# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserConsulting(models.Model):
    consulting_company = models.ForeignKey(
        'company.ConsultingCompany'
    )
    user = models.OneToOneField(
        User,
        related_name='user_consulting'
    )
    position = models.CharField(
        max_length=100
    )

    def __unicode__(self):
        return '%s - %s' % (self.user, self.consulting_company)


class Customer(models.Model):
    consulting_company = models.ForeignKey(
        'company.ConsultingCompany'
    )
    number_ruc = models.CharField(
        max_length=11
    )
    name = models.CharField(
        max_length=100
    )
    number_telephone = models.CharField(
        max_length=9
    )

    def __unicode__(self):
        return '%s - %s' % (self.name, self.consulting_company)
