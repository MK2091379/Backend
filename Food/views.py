from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from Register.models import Company,User
from .models import Food
from .serializers import FoodSerializer
from automation.permissions import IsCompanyOwner,IsEmployee



class FoodViewSetManager(ModelViewSet):
    permission_classes = [IsAuthenticated,IsCompanyOwner]
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
    def put_food(self,request,id):
        if request.method == 'PUT':
            food = Food.objects.get(id=id)
            serializer = FoodSerializer(food, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    @action(detail=False, methods=['DELETE'])
    def delete_food(self,request,id):
        if request.method == 'DELETE':
            Food.objects.get(id=id).delete()
            return Response("OK")
    #################################################################################################
    @action(detail=False, methods=['GET'])
    def reserve_food_manager(self,request,id):
        if request.method == 'GET':
            food = Food.objects.get(id=id)
            food.amount-=1
            food.save()
            return Response("OK")
    @action(detail=False, methods=['DELETE'])
    def delete_reserved_food_manager(self,request,id):
        if request.method == 'DELETE':
            food = Food.objects.get(id=id)
            food.amount+=1
            food.save()
            return Response("OK")
class FoodViewSetEmployee(ModelViewSet):
    #user,name,date,amount,company
    permission_classes = [IsAuthenticated,IsEmployee]
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    @action(detail=False, methods=['GET'])
    def reserve_food_employee(self,request,id):
        if request.method == 'GET':
            food = Food.objects.get(id=id)
            food.amount-=1
            food.save()
            return Response("OK")
    @action(detail=False, methods=['DELETE'])
    def delete_reserved_food_employee(self,request,id):
        if request.method == 'DELETE':
            food = Food.objects.get(id=id)
            food.amount+=1
            food.save()
            return Response("OK")
    @action(detail=False, methods=['GET'])
    def get_company_food_employee(self, request):
        if request.method == 'GET':
            food = Food.objects.filter(company = request.user.company)
            serializer = FoodSerializer(food,many=True)
            return Response(serializer.data)
