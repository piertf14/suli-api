# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from project.models import Project
from project.serializers import ProjectSerializers
from rest_framework import permissions
from oauth2_provider.contrib.rest_framework import TokenHasScope


class ListProjectsAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['read']

    def get(self, request, pk, format=None):
        projects = Project.objects.filter(
            consulting_company__id=pk,
            status__slug='new'
        )
        serializers = ProjectSerializers(projects, many=True)
        return Response(serializers.data)