# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ConsultingCompany(models.Model):
    number_ruc = models.CharField(
        max_length=11
    )
    name = models.CharField(
        max_length=100
    )
    number_telephone = models.CharField(
        max_length=9
    )
    address = models.CharField(
        max_length=250
    )
    email = models.EmailField()
    contact = models.CharField(
        max_length=150
    )
    position_name = models.CharField(
        max_length=150
    )

    def __unicode__(self):
        return '%s - %s' % (self.number_ruc, self.name)


class MiningUnit(models.Model):
    customer = models.ForeignKey(
        'customer.Customer',
        related_name='customer_mining_unit'
    )
    name = models.CharField(
        max_length=150
    )

    def __unicode__(self):
        return self.name
