# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Instrument, InstrumentCertificate


class InstrumentCertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstrumentCertificate
        fields = '__all__'


class InstrumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instrument
        fields = '__all__'