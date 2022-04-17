from requests import request
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    priority=serializers.IntegerField()
    description=serializers.CharField(max_length=None)
    checkbox=serializers.BooleanField() 
    class Meta:
        model=Task
        fields=['priority','description','checkbox','user_id']
 
    # def checking_checkbox(self,Task:Task):
    #     if(Task.creation_time==datetime.now()):
    #          Task.checkbox=False
    
   
   
    # def validate(self, attrs):
    #     if attrs['priority']<=0:
    #         return serializers.ValidationError("priority must be positive")
    
   
        
        
    
