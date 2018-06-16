# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Project, StatusProject
from customer.serializers import CustomerSerializers


class StatusProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = StatusProject
        fields = '__all__'


class ProjectSerializers(serializers.ModelSerializer):
    status = StatusProjectSerializers()
    customer = CustomerSerializers()

    class Meta:
        model = Project
        exclude = ['consulting_company']
