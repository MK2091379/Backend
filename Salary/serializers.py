from pyexpat import model
from rest_framework import serializers
from .models import EmployeeSalary
from Register.models import User 



class AddEmployeeSalarySerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        
        
        model=EmployeeSalary
        fields=['id','salary_hours','price_food','price_transportatio','price_dormitory']
        read_only_fields=['id']
        
        