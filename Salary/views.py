from calendar import month
from logging.handlers import TimedRotatingFileHandler
from urllib import response
from webbrowser import get
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from requests import request
from rest_framework.viewsets import  ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from TimeAndDateTracker.models import TimeAndDateTracker

from Register.models import User
from .serializers import AddEmployeeSalarySerializer,ShowMySalarySeriializer
from .models import EmployeeSalary
# Create your views here.



class AdminSalaryAPI(ModelViewSet):
    serializer_class=AddEmployeeSalarySerializer
    queryset=EmployeeSalary.objects.all()
    
    
    @action(detail=False,methods=['POST','PATCH'])
    def add_salary_for_employee(self,request,id):
     if request.method=='POST':
        employeesalary=EmployeeSalary.objects.create(employee_id=id)
        serializer=AddEmployeeSalarySerializer(employeesalary,many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response(status=status.HTTP_201_CREATED)
        
     elif request.method=="PATCH":
         getsalaryuser=get_object_or_404(EmployeeSalary,user_id=id)
         serializer=AddEmployeeSalarySerializer(getsalaryuser,data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return response(status=status.HTTP_200_OK)
         

class EomplyeeShowSalary(ModelViewSet):
    
    serializer_class=ShowMySalarySeriializer
    queryset=EmployeeSalary.objects.all()
    action(detail=False,methods=['GET'])
    def show_my_salary(self , request):
       total_hour=0
       
       now=datetime.now()
       now_year=now.year
       now_month=now.month
       
       
       settimetracker=TimeAndDateTracker.objects.filter(user_id=request.user.id 
                                                        ,created_date__year=now_year,created_date__month=now_month)
       
       for track in settimetracker:
           total_hour+=track.time_minus()
           
       print(total_hour)   
        
       getsalary=get_object_or_404(EmployeeSalary,employee_id=request.user.id)
       serializer=ShowMySalarySeriializer(getsalary,many=False)
       new_serializer={ 
                       "salary":serializer.data["monthly_salary"],
                       "health_insurance":"100" ,
                       "time":str(total_hour),
       }
       return Response(new_serializer) 
       
       
        
        
         
        
        
       
     
    #    return Response(serializer.data)
        
        
    
    