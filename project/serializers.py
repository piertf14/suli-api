# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Project, StatusProject
from customer.serializers import CustomerSerializer
from company.serializers import MiningUnitSerializer


class StatusProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusProject
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    status = StatusProjectSerializer()
    customer = CustomerSerializer()
    mining_units = serializers.SerializerMethodField()

    def get_mining_units(self, obj):
        mining_units = [project_detail.mining_init for project_detail in obj.project_detail_project.all()]
        if len(mining_units) > 0:
            serializer = MiningUnitSerializer(mining_units, many=True, context={
                'detail_project':  obj.project_detail_project.first().pk})
            return serializer.data
        return None

    class Meta:
        model = Project
        exclude = ['consulting_company']
