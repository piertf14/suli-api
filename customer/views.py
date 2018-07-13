# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from oauth2_provider.contrib.rest_framework import TokenHasScope
from core.utils import get_access_token
from .serializers import UserConsultingSerializer


class MyUserAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['read']

    def get(self, request, format=None):
        try:
            user = get_access_token(request).user.user_consulting
        except:
            user = None
        serializer = UserConsultingSerializer(user, many=False)
        return Response(serializer.data)
