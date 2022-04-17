from asyncio import tasks
from django.shortcuts import get_object_or_404
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from ToDoList import serializers
from rest_framework import status



# Create your views here.

 

@api_view(['GET','POST'])    
def todo_view_list(request,id):
   
    if request.method=='GET':
         queryset=Task.objects.filter(user_id=id)
         serializer=TaskSerializer(queryset,many=True)
         return Response(serializer.data)
    elif request.method=='POST':
         serializer=TaskSerializer(data=request.data,user_id=id)
         serializer.is_valid(raise_exception=True)
         serializer.save() 
         return Response('ok')


# @api_view(['GET','DELETE'])    
# def todo_view_dataile(request,id1,id2):
#     result=Task.objects.filter(user_id=id1).get(pk=id2)
#     if request.method=='GET':   
#              serializer=TaskSerializer(result)
#              return Response(serializer.data)
#     elif request.method=='DELETE':
#             result.delete()
#             return Response("ok")
    
              
        
   
     




   
 
    
    

        
