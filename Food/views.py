from unicodedata import name
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from urllib import request, response
from .models import Food
from .serializers import FoodSerializer
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



class FoodViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    @action(detail=False, methods=['GET'])
    def get_food_manager(self, request):
        if request.method == 'GET':
            food = Food.objects.filter(pk = request.user.pk)
            serializer = FoodSerializer(food,many=True)
            return Response(serializer.data)
    @action(detail=False, methods=['POST'])
    def post_food(self,request):
        if request.method == 'POST':
            food = Food.objects.create(user_id = request.user.id)
            #food.company.add(request.user.company.company_name)
            serializer = FoodSerializer(food, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    @action(detail=False, methods=['PUT'])
    def put_food(self,request):
        if request.method == 'PUT':
            food = Food.objects.get(user_id = request.user.id)
            serializer = FoodSerializer(food, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    @action(detail=False, methods=['DELETE'])
    def delete_food(self,request,name):
        if request.method == 'DELETE':
            Food.objects.get(name=name).delete()
            return Response("OK")
            #serializer = FoodSerializer(food, data=request.data)
            #serializer.is_valid(raise_exception=True)
            #serializer.save()
            #return Response(serializer.data)