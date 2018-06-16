# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserConsulting(models.Model):
    consulting_company = models.ForeignKey(
        'company.ConsultingCompany'
    )
    user = models.ForeignKey(
        User
    )
    position = models.CharField(
        max_length=100
    )


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
