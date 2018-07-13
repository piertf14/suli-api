# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from oauth2_provider.contrib.rest_framework import TokenHasScope

from core.utils import get_access_token
from .models import Agent, ReferentialImage, MeasurementValue
from .serializers import AgentSerializer, ChainCustodySerializer, ChainCustodyRegisterSerializer, \
    MeasurementValueSerializers, ReferentialImageSerializers


class AgentAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['read']

    def get(self, request, format=None):
        agents = Agent.objects.all()
        serializers = AgentSerializer(agents, many=True)
        return Response(serializers.data)


class CustodyChainAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['read', 'write']

    def post(self, request, format=None):
        try:
            request_data = request.data
            user = get_access_token(request).user.user_consulting
            request_data.update({"user": user.id})
            serializer = ChainCustodyRegisterSerializer(data=request_data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)
            custody_chain = serializer.save()

            serializer = ChainCustodySerializer(custody_chain, many=False)
            return Response(serializer.data)

        except Exception as e:
            return Response({"message": e.message}, status=400)


class MeasurementValueAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['read', 'write']

    def post(self, request, format=None):
        try:
            request_data = request.data
            serializer = MeasurementValueSerializers(data=request_data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)
            measurement_value = serializer.save()

            serializer = MeasurementValueSerializers(measurement_value, many=False)
            return Response(serializer.data)

        except Exception as e:
            return Response({"message": e.message}, status=400)


class ReferentialImageAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['read', 'write']

    def post(self, request, format=None):
        try:
            measurement_value = MeasurementValue.objects.get(pk=request.data['measurement_value'])
            referential_image = ReferentialImage(image=request.data['images'],
                                                 measurement_value=measurement_value)
            referential_image.save()

            serializer = ReferentialImageSerializers(referential_image, many=False)
            return Response(serializer.data)
        except Exception as e:
            return Response({'message': e.message}, status=400)