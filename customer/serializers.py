# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, UserConsulting
from company.serializers import ConsultingCompanySerializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class UserConsultingSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    consulting_company = ConsultingCompanySerializers()

    class Meta:
        model = UserConsulting
        fields = '__all__'
