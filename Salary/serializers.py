from rest_framework import serializers
from .models import EmployeeSalary
from Register.models import User 
from TimeAndDateTracker.models import TimeAndDateTracker
from Transportation.models import AdminTransportation
from Transportation.serializers import PriceTransportationSerializer






        
        
    
            
class UserPrices(serializers.ModelSerializer):
        admintranslates=PriceTransportationSerializer(many=True)
        class Meta:
                model=User
                fields=['admintranslates']
                
class AddEmployeeSalarySerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model=EmployeeSalary
        fields=['id','employee','monthly_salary','reward_benefit','min_working',]
        read_only_fields=['id','employee']
        
class ShowMySalarySeriializer(serializers.ModelSerializer):
    

    class Meta:
        model=EmployeeSalary
        fields=['monthly_salary','min_working']
        read_only_fields=['monthly_salary','min_working']
        
 
    