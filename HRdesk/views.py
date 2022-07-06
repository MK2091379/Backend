from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from urllib import request, response
from Register.models import User
from .serializers import HRdeskSerializer
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class HRDeskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = HRdeskSerializer
    @action(detail=False, methods=['GET'])
    def get_employee(self, request):
        if request.method == 'GET':
            tracker = User.objects.filter(role = 'E')
            serializer = HRdeskSerializer(tracker,many=True)
            return Response(serializer.data)