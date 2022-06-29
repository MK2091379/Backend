from rest_framework import serializers
from . import models
from Register.models import User


class UserServiceCounterSerializer(serializers.ModelSerializer):

        class Meta:
            model=User
            fields=['email','last_name','first_name']
            extra_kwargs = {       'email': {'read_only': True},
                               'last_name': {'read_only': True},
                               'first_name': {'read_only': True},
                               }

class RequestSerializer(serializers.ModelSerializer):
    
    user=UserServiceCounterSerializer(many=True)
    class Meta:
        model=models.RequestForm
        fields=['id','title_form','user','status','type_form','value_form']
        read_only_fields=['id']

class ResponseSerializer(serializers.ModelSerializer):
    
    user=UserServiceCounterSerializer(many=True)
    class Meta:
        model=models.RequestForm
        fields=['title_form','user','status','type_form','value_form']
        extra_kwargs = {       'id': {'read_only': True},
                               'title_form': {'read_only': True},
                               'user': {'read_only': True},
                               'type_form': {'read_only': True},
                               'value_form': {'read_only': True},
                               }
        
    
        