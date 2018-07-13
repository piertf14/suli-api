# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from oauth2_provider.contrib.rest_framework import TokenHasScope

from project.models import Project
from project.serializers import ProjectSerializer


class ListProjectsAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['read']
    company = None

    def get_company(self):
        try:
            self.company = self.request.user.user_consulting.consulting_company
        except Exception as e:
            return Response({'message': e.message}, status=400)

    def get(self, request, format=None):
        self.get_company()
        projects = Project.objects.filter(
            consulting_company=self.company,
            status__slug='new'
        )
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)