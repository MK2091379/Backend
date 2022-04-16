from webbrowser import get
from django.shortcuts import get_object_or_404
from Register.models import User
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from ToDoList import serializers
from rest_framework import status
# Create your views here.

 

@api_view(['GET','POST','DELETE'])    
def todo_view(request,id):
     queryset=Task.objects.filter(user_id=id)
     serializer=TaskSerializer(queryset,many=True)
     return Response(serializer.data)




   
 
    
    

        
