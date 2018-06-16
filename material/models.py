# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Instrument(models.Model):
    name = models.CharField(
        max_length=100
    )
    brand = models.CharField(
        max_length=100
    )
    model = models.CharField(
        max_length=100
    )
    series = models.CharField(
        max_length=100
    )
    code_certification = models.PositiveIntegerField()


class InstrumentCertificate(models.Model):
    instrument = models.ForeignKey(
        Instrument
    )
    certificate_calibration = models.PositiveIntegerField()
    due_calibration = models.DateField()
