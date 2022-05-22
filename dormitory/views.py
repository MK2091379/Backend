from unicodedata import name
from django.shortcuts import render
from pkg_resources import declare_namespace
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from urllib import request, response
from Register.models import Company
from .models import Dormitory
from .serializers import DormitorySerializer
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



class DormitoryViewSetManager(ModelViewSet):
    #user,name,date,amount,company
    permission_classes = [IsAuthenticated]
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer
    @action(detail=False, methods=['GET'])
    def get_dormitory_manager(self, request):
        if request.method == 'GET':
            dormitory = Dormitory.objects.filter(user_id = request.user.id)
            serializer = DormitorySerializer(dormitory,many=True)
            return Response(serializer.data)
    @action(detail=False, methods=['POST'])
    def post_dormitory(self,request):
        if request.method == 'POST':
            dormitory = Dormitory.objects.create(user_id = request.user.id)
            serializer = DormitorySerializer(dormitory, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    @action(detail=False, methods=['PUT'])
    def put_dormitory(self,request,number,capacity):
        if request.method == 'PUT':
            dormitory = Dormitory.objects.get(number = number,capacity = capacity,user_id = request.user.id)
            serializer = DormitorySerializer(dormitory, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    @action(detail=False, methods=['DELETE'])
    def delete_dormitory(self,request,number,capacity):
        if request.method == 'DELETE':
            Dormitory.objects.get(number = number,capacity = capacity,user_id = request.user.id).delete()
            return Response("OK")
    #################################################################################################
    #def get_reserved_food_manager(self, request,company):
    #    if request.method == 'GET':
    #        food = Food.objects.filter(user_id = request.user.id,company = company)
    #        serializer = FoodSerializer(food,many=True)
    #        return Response(serializer.data)
    @action(detail=False, methods=['GET'])
    def reserve_dormitory_manager(self,request,number,company):
        if request.method == 'GET':
            dormitory = Dormitory.objects.get(number = number,company=company)
            if (dormitory.capacity >0):
                dormitory.capacity-=1
                dormitory.save()
                return Response("OK")
            else:
                return Response("The room is feel")
    @action(detail=False, methods=['GET'])
    def delete_reserved_dormitory_manager(self,request,number,company):
        if request.method == 'GET':
            dormitory = Dormitory.objects.get(number = number,company=company)
            dormitory.amount+=1
            dormitory.save()
            return Response("OK")
class DormitoryViewSetEmployee(ModelViewSet):
    #user,name,date,amount,company
    permission_classes = [IsAuthenticated]
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer
    @action(detail=False, methods=['POST'])
    def reserve_dormitory_employee(self,request,number,date,company):
        if request.method == 'GET':
            dormitory = Dormitory.objects.get(number = number,company=company)
            if (dormitory.capacity >0):
                dormitory.capacity-=1
                dormitory.save()
                return Response("OK")
            else:
                return Response("The room is feel")
    @action(detail=False, methods=['GET'])
    def delete_reserved_dormitory_employee(self,request,number,date,company):
        if request.method == 'GET':
            dormitory = Dormitory.objects.get(number = number,company=company)
            dormitory.amount+=1
            dormitory.save()
            return Response("OK")