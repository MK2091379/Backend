from requests import request
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    priority=serializers.IntegerField()
    description=serializers.CharField(max_length=None)
    checkbox=serializers.BooleanField() 
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model=Task
        fields=['id','priority','description','checkbox','user_id']
class TaskUpdatingSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only = False)
    class Meta:
        model = Task
        fields = ['id','priority','description','checkbox','user_id']
    
   
        
        
    
