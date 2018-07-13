# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer, UserConsulting
from company.serializers import ConsultingCompanySerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class UserConsultingSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    consulting_company = ConsultingCompanySerializer()

    class Meta:
        model = UserConsulting
        fields = '__all__'
