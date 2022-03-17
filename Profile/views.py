from urllib import request
from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Employee,CompanyOwner
from .serializers import EmployeeSerializer,CompanyOwnerSerializer


class EmployeeView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
class CompanyView(generics.ListAPIView):
    queryset = CompanyOwner.objects.all()
    serializer_class = CompanyOwnerSerializer













