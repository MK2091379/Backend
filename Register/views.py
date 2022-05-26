#from django.shortcuts import render
from django.conf import UserSettingsHolder
from requests import request
from rest_framework import generics,permissions,status
from .models import Company, User
from rest_framework.viewsets import ModelViewSet
from .serializers import  EmployeeSerializer,CompnyOwnerSerializer,CompanySerializer,CompanyGetSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

#from rest_framework.response import Response
#from rest_framework.views import APIView


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
    
class GetmyRole(ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=User.objects.all()
    @action(detail=False,methods=['GET'])
    def getrole(self,request):
        user=User.objects.get(id=request.user.id)
        return Response(user.role)
        
class GetAllCompany(ModelViewSet):
    queryset=Company.objects.all()
    @action(detail=False,methods=['GET'])
    def getcompany(self,request):
        queryset=Company.objects.all()
        serializer = CompanyGetSerializer(queryset,many=True)
        return Response(serializer.data)

    

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






