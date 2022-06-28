from curses import meta
from dataclasses import field
from rest_framework import serializers
from . import models
from Register.models import User


class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model=User
            fields=['email','last_name','first_name']

class RequestSerializer(serializers.ModelSerializer):
    
    user=UserSerializer(many=True)
    class Meta:
        model=models.RequestForm
        fields=['id','title','user','status','type_form','value_form']
        read_only_fields=['id']

class ResponseSerializer(serializers.ModelSerializer):
    
    user=UserSerializer(many=True)
    class Meta:
        model=models.RequestForm
        fields=['title','user','status','type_form','value_form']
        extra_kwargs = {       'id': {'read_only': True},
                               'title': {'read_only': True},
                               'user': {'read_only': True},
                               'type_form': {'read_only': True},
                               'value_form': {'read_only': True},
                               }
        
    
        