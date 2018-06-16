# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import ConsultingCompany


class ConsultingCompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = ConsultingCompany
        fields = '__all__'
