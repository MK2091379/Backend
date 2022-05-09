from rest_framework import serializers
from .models import AdminTransportation,TransportationsRequest


class AdminTransportationSerializer(serializers.ModelSerializer):
        
    
    class Meta:
        model=AdminTransportation
        fields=['id','address',
                'maximum_capacity','details',
                 'address_search','location',
                'arrival_time','Return_time']
        
        read_only_fields = ['id']

class RequestTransportationSerializer(serializers.ModelSerializer):  
    
    class Meta:
        model=TransportationsRequest
        fields=['id','request']
        read_only_fields = ['id']