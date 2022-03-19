from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Company, User
from .serializers import  EmployeeSerializer,CompnyOwnerSerializer,CompanySerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateEmployeeView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer
    permissions.IsAuthenticatedOrReadOnly


class CreateCompanyView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permissions.IsAuthenticatedOrReadOnly



class CompanyOwnerView(generics.ListCreateAPIView):

    queryset=User.objects.all()
    serializer_class=CompnyOwnerSerializer
    permissions.IsAuthenticatedOrReadOnly
    

    # def get(self,format=None):

    #     queryset = User.objects.all()
    #     serializer = CompnyOwnerSerializer(queryset,many=True)
    #     return Response(serializer.data)

    # def post(self, request):

    #     serializer =CompnyOwnerSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=ValueError):
    #         serializer.create(validated_data=request.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.error_messages,
    #                     status=status.HTTP_400_BAD_REQUEST)






