from asyncio import events
from multiprocessing import Event
from urllib import request
from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Employee,CompanyOwner
from .serializers import  EmployeeProfileSerializer,CompanyOwnerProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeProfileSerializer
    @action(detail=False, methods=['GET', 'PUT','PATCH','DELETE'])
    def me(self, request):
        (employee, created) = Employee.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = EmployeeProfileSerializer(employee)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = EmployeeProfileSerializer(employee, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'DELETE':
            Employee.objects.get(user_id=employee).delete()
            return Response("ok")
        #elif request.method == 'PATCH':
        #   employee_updated = Employee.objects.filter(user_id=request.user.id)
        #   serializer = EmployeeProfileSerializer(employee_updated)
        #   serializer.is_valid(raise_exception=True)
        #   serializer.save()
        #   return Response(serializer.data)






