from pickle import TRUE
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import  ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from Transportation.models import AdminTransportation
from TimeAndDateTracker.models import TimeAndDateTracker
from .serializers import AddEmployeeSalarySerializer,ShowMySalarySeriializer
from .models import EmployeeSalary
from datetime import datetime
# Create your views here.

from rest_framework.pagination import PageNumberPagination




class AdminSalaryAPI(ModelViewSet):
    serializer_class=AddEmployeeSalarySerializer
    queryset=EmployeeSalary.objects.all()
    
    
    @action(detail=False,methods=['PATCH'])
    def add_salary_for_employee(self,request,id):
    #  if request.method=='POST':
    #     employeesalary=EmployeeSalary.objects.create(employee_id=id)
    #     serializer=AddEmployeeSalarySerializer(employeesalary,many=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return response(status=status.HTTP_201_CREATED)
        
    #  elif request.method=="PATCH":
         getsalaryuser=get_object_or_404(EmployeeSalary,user_id=id)
         serializer=AddEmployeeSalarySerializer(getsalaryuser,data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(status=status.HTTP_200_OK)
class AdminSalaryAPI(ModelViewSet):
    serializer_class=AddEmployeeSalarySerializer
    queryset=EmployeeSalary.objects.all()
    pagination_class=PageNumberPagination
    
    @action(detail=False,methods=['PATCH'])
    def add_salary_for_employee(self,request,id):
   
         getsalaryuser=get_object_or_404(EmployeeSalary,user_id=id)
         serializer=AddEmployeeSalarySerializer(getsalaryuser,data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(status=status.HTTP_200_OK)
     
    @action(detail=False,methods=['GET'])
    def get_my_employee_salary(self,request):
        pagiantor=PageNumberPagination()
        pagiantor.page_size=10
        getsalaryuser=pagiantor.paginate_queryset(EmployeeSalary.objects.filter(
            employee__company=request.user.company),request)
        if getsalaryuser.exists():
            serializer=AddEmployeeSalarySerializer(getsalaryuser,many=True)
            return pagiantor.get_paginated_response(serializer.data)
        else:
             return Response(status=status.HTTP_404_NOT_FOUND)
        

         

class EomplyeeShowSalary(ModelViewSet):
    
    serializer_class=ShowMySalarySeriializer
    queryset=EmployeeSalary.objects.all()
    action(detail=False,methods=['GET'])
    def show_my_salary(self , request):
       total_hour=0
       total_cost_transportation=0.0
       now=datetime.now()
       now_year=now.year
       now_month=now.month
       
       
       settimetracker=TimeAndDateTracker.objects.filter(user_id=request.user.id 
                                                        ,created_date__year=now_year,created_date__month=now_month)
       
       list_transporttion=AdminTransportation.objects.filter(user__id=request.user.id)
       #ttal hour of time tracker 
       for track in settimetracker:
           total_hour+=track.time_minus()
           #total price teansporation 
       for price in list_transporttion:
            total_cost_transportation=price.getter_price()
           
       print(total_hour)   
        
       getsalary=get_object_or_404(EmployeeSalary,employee_id=request.user.id)
       serializer=ShowMySalarySeriializer(getsalary,many=False)
       new_serializer={ 
                       "monthly_salary":serializer.data["monthly_salary"],
                       "min_time":serializer.data["min_working"],
                       "health_insurance":100,
                       "total_time":total_hour,
                       "dormitory":0.0,
                       "food":0.0,
                       "Transportation":total_cost_transportation
       }
       return Response(new_serializer) 
       
       
        
        
         
        
        
       
     
    #    return Response(serializer.data)
        
        
    
    