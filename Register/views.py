from django.shortcuts import render
from rest_framework import generics,permissions
from .models import User,Company
from .serializers import UserSerializer,CompanySerializer

# Create your views here.
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class UserList2(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions.IsAuthenticatedOrReadOnly
    
    
    
    
