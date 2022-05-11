from rest_framework import serializers
from .models import AdminTransportation,RequestUser


class AdminTransportationSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model=AdminTransportation
        fields=['id','address',
                'maximum_capacity','details',
                 'address_search','location',
                'arrival_time','Return_time','saturday','sunday','monday','tuesday','wednesday','thursday','friday']
        
        read_only_fields = ['id']

class RequestUserSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model=RequestUser
        fields=['id','request','type_of_service']
        read_only_fields = ['id']


class ResponseApiSerializer(serializers.ModelSerializer):
    pass