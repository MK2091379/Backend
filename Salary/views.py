from urllib import response
from webbrowser import get
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from requests import request
from rest_framework.viewsets import  ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from Register.models import User
from .serializers import AddEmployeeSalarySerializer
from .models import EmployeeSalary
# Create your views here.



class AdminSalaryAPI(ModelViewSet):
    serializer_class=AddEmployeeSalarySerializer
    queryset=EmployeeSalary.objects.all()
    
    
    @action(detail=False,methods=['POST','PATCH'])
    def add_salary_for_employee(self,request,id):
     if request.method=='POST':
        addsalary=EmployeeSalary.objects.create(user_id=id)
        serializer=AddEmployeeSalarySerializer(addsalary,many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response(status=status.HTTP_201_CREATED)
        
     elif request.method=="PATCH":
         getsalaryuser=get_object_or_404(EmployeeSalary,user_id=id)
         serializer=AddEmployeeSalarySerializer(getsalaryuser,data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return response(status=status.HTTP_200_OK)
         

class EomplyeeShowSalary(ModelViewSet)
    
    