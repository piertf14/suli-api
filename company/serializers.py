# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import ConsultingCompany, MiningUnit
from evaluation.models import ChainCustody
from evaluation.serializers import ChainCustodySerializer


class ConsultingCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultingCompany
        fields = '__all__'


class MiningUnitSerializer(serializers.ModelSerializer):
    chain_custody = serializers.SerializerMethodField()

    def get_chain_custody(self, obj):
        chain_custody = ChainCustody.objects.filter(detail_project=self.context.get('detail_project'))
        serializer = ChainCustodySerializer(chain_custody, many=True)
        return serializer.data

    class Meta:
        model = MiningUnit
        fields = '__all__'
