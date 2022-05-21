from unicodedata import name
from django.shortcuts import render
from pkg_resources import declare_namespace
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from urllib import request, response

from Register.models import Company
from .models import Food
from .serializers import FoodSerializer
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



class FoodViewSetManager(ModelViewSet):
    #user,name,date,amount,company
    permission_classes = [IsAuthenticated]
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    @action(detail=False, methods=['GET'])
    def get_food_manager(self, request):
        if request.method == 'GET':
            food = Food.objects.filter(user_id = request.user.id)
            serializer = FoodSerializer(food,many=True)
            return Response(serializer.data)
    @action(detail=False, methods=['POST'])
    def post_food(self,request):
        if request.method == 'POST':
            food = Food.objects.create(user_id = request.user.id)
            serializer = FoodSerializer(food, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    @action(detail=False, methods=['PUT'])
    def put_food(self,request,name,date):
        if request.method == 'PUT':
            food = Food.objects.get(name=name,date=date,user_id = request.user.id)
            serializer = FoodSerializer(food, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    @action(detail=False, methods=['DELETE'])
    def delete_food(self,request,name,date):
        if request.method == 'DELETE':
            Food.objects.get(name=name,date=date,user_id = request.user.id).delete()
            return Response("OK")
    #################################################################################################
    #def get_reserved_food_manager(self, request,company):
    #    if request.method == 'GET':
    #        food = Food.objects.filter(user_id = request.user.id,company = company)
    #        serializer = FoodSerializer(food,many=True)
    #        return Response(serializer.data)
    @action(detail=False, methods=['GET'])
    def reserve_food_manager(self,request,name,date,company):
        if request.method == 'GET':
            food = Food.objects.get(name=name,company=company,date=date)
            food.amount-=1
            food.save()
            return Response("OK")
    @action(detail=False, methods=['GET'])
    def delete_reserved_food_manager(self,request,name,date,company):
        if request.method == 'GET':
            food = Food.objects.get(name=name,company=company,date=date)
            food.amount+=1
            food.save()
            return Response("OK")
class FoodViewSetEmployee(ModelViewSet):
    #user,name,date,amount,company
    permission_classes = [IsAuthenticated]
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    @action(detail=False, methods=['POST'])
    def reserve_food_employee(self,request,name,date,company):
        if request.method == 'GET':
            food = Food.objects.get(name=name,company=company,date=date)
            food.amount-=1
            food.save()
            return Response("OK")
    @action(detail=False, methods=['GET'])
    def delete_reserved_food_employee(self,request,name,date,company):
        if request.method == 'GET':
            food = Food.objects.get(name=name,company=company,date=date)
            food.amount+=1
            food.save()
            return Response("OK")