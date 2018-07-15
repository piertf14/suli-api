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


class MeasurementValueV2Serializers(serializers.ModelSerializer):
    referential_image = serializers.SerializerMethodField()

    def get_referential_image(self, obj):
        referential_image = obj.measurement_value_referential_image.all()
        if referential_image.exists():
            serializer = ReferentialImageSerializers(referential_image.first(), many=False)
            return serializer.data
        return None

    class Meta:
        model = MeasurementValue
        fields = '__all__'


def measurement_value_parse_data(args):
    dict = {}
    dict['chain_custody'] = args.data['chain_custody']
    dict['max'] = args.data['max']
    dict['min'] = args.data['min']
    dict['avg'] = args.data['avg']
    dict['point_reference'] = args.data['point_reference']
    dict['observation_measurement'] = args.data['observation_measurement']
    dict['type_lighting'] = args.data['type_lighting']
    return dict