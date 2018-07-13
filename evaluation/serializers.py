# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import ChainCustody, Agent, MeasurementValue, ReferentialImage


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = '__all__'


class ChainCustodyRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChainCustody
        fields = '__all__'


class ChainCustodySerializer(serializers.ModelSerializer):
    agent = AgentSerializer()

    class Meta:
        model = ChainCustody
        fields = '__all__'


class MeasurementValueSerializers(serializers.ModelSerializer):

    class Meta:
        model = MeasurementValue
        fields = '__all__'


class ReferentialImageSerializers(serializers.ModelSerializer):

    class Meta:
        model = ReferentialImage
        fields = '__all__'
