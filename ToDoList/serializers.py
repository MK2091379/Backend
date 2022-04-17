from datetime import datetime
from wsgiref import validate
from requests import request
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.Serializer):
    priority=serializers.IntegerField()
    description=serializers.CharField(max_length=None)
    checkbox=serializers.BooleanField() 
 
    # def checking_checkbox(self,Task:Task):
    #     if(Task.creation_time==datetime.now()):
    #          Task.checkbox=False
    
    def create(self, validated_data):
        task=Task(**validated_data)
        task.checkbox=False
        task.user_id=1
        task.save()
        return task
   
    # def validate(self, attrs):
    #     if attrs['priority']<=0:
    #         return serializers.ValidationError("priority must be positive")
    
   
        
        
    
