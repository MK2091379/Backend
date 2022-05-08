from rest_framework import serializers
from .models import AdminTransportation


class AdminTransportationSerializer(serializers.ModelSerializer):
        
    
    class Meta:
        model=AdminTransportation
        fields=['id','address',
                'maximum_capacity','details',
                 'address_search','location',
                'arrival_time','Return_time']
        
        read_only_fields = ['id']