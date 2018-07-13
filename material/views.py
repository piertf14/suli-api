# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from oauth2_provider.contrib.rest_framework import TokenHasScope

from .serializers import InstrumentSerializer
from .models import Instrument


class InstrumentAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['read']

    def get(self, request, format=None):
        instruments = Instrument.objects.all()
        serializers = InstrumentSerializer(instruments, many=True)
        return Response(serializers.data)