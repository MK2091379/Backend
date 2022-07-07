from rest_framework import serializers
from .models import AdminTransportation
from Register.models import User
from Register.serializers import EmployeeSerializer


class AdminTransportationSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model=AdminTransportation
        fields=['id','address',
                'maximum_capacity','details',
                 'address_search','location',
                'arrival_time','Return_time',
                'saturday', 'sunday', 'monday', 'tuesday',
                'wednesday', 'thursday', 'friday','monthly_price']
        
        read_only_fields = ['id']
        
        
class EmployeeGetSerializer(serializers.ModelSerializer):
    user=EmployeeSerializer(many=True)
    class Meta:
        model=AdminTransportation
        fields=['id','address','maximum_capacity',
                'details','arrival_time',
                'Return_time','user',
                'saturday', 'sunday', 'monday', 'tuesday',
                'wednesday', 'thursday', 'friday','monthly_price']
        
        extra_kwargs = {       'id': {'read_only': True},
                               'address': {'read_only': True},
                               'maximum_capacity': {'read_only': True},
                               'details': {'read_only': True},
                               'arrival_time': {'read_only': True},
                               'Return_time': {'read_only': True},
                               'monthly_price': {'read_only': True},

                               }


class UserTransportationSerializer(serializers.ModelSerializer):
        admintranslates=AdminTransportationSerializer(many=True)
        class Meta:
                model=User
                fields=['admintranslates']
 
                
class PriceTransportationSerializer(serializers.ModelSerializer):
        class Meta:
            model=AdminTransportation
            fields=['monthly_price']
            read_only_fields=['monthly_price']
                

# class EmployeeGetServicesSerializer(serializers.ModelSerializer):
   
#     class Meta:
#         model=AdminTransportation
#         fields=['id','address','maximum_capacity',
#                 'details','arrival_time',
#                 'Return_time','user']
        
#         extra_kwargs = {       'id': {'read_only': True},
#                                'address': {'read_only': True},
#                                'maximum_capacity': {'read_only': True},
#                                'details': {'read_only': True},
#                                'arrival_time': {'read_only': True},
#                                'Return_time': {'read_only': True},
#                                }


# class RequestUserSerializer(serializers.ModelSerializer):  
    
#     class Meta:
#         model=RequestUser
#         fields=['id','request','type_of_service']
#         read_only_fields = ['id']


# class ResponseApiSerializer(serializers.ModelSerializer):
#     pass
