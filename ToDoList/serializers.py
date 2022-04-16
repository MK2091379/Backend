from ast import Return
from datetime import datetime
from asyncio import tasks
from tkinter import N
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.Serializer):
    description=serializers.CharField(max_length=None)
    checkbox=serializers.BooleanField()
    deadline=serializers.DateTimeField()  
    # def checking_checkbox(self,Task:Task):
    #     if(Task.creation_time==datetime.now()):
    #          Task.checkbox=False
        
    
