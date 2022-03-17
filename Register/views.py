from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Company, User
from .serializers import  EmployeeSerializer,CompnyOwnerSerializer,CompanySerializer


class CreateEmployeeView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer
    permissions.IsAuthenticatedOrReadOnly
class CreateCompanyOwnerView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CompnyOwnerSerializer
    permissions.IsAuthenticatedOrReadOnly
class CreateCompanyView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permissions.IsAuthenticatedOrReadOnly
    
    
    
    
