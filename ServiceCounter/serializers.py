from rest_framework import serializers
from .models import *




class RequestSerializer(serializers.ModelSerializer):
    
        class Meta:
            model=RequestForm
            fields=['id','title_form','status','type_form','value_form']
            read_only_fields=['id','status']

class ResponseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=RequestForm
        fields=['id','title_form','user','status','type_form','value_form','created_time']
        
        extra_kwargs = {      
                               'title_form': {'read_only': True},
                               'user': {'read_only': True},
                               'type_form': {'read_only': True},
                               'value_form': {'read_only': True},
                               'created_time': {'read_only': True},
                               }
        
    
        