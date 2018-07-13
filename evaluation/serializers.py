# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import ChainCustody, Agent


class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = '__all__'


class ChainCustodySerializer(serializers.ModelSerializer):
    agent = AgentSerializer()

    class Meta:
        model = ChainCustody
        fields = '__all__'