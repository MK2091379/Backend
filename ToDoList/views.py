from django.shortcuts import get_object_or_404

import ToDoList
from .models import Task
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from .serializers import TaskSerializer
from ToDoList import serializers
from rest_framework import status
from rest_framework.viewsets import ModelViewSet



# Create your views here.

class ToDoListViewSet(ModelViewSet):
     queryset = Task.objects.all()
     serializer_class =TaskSerializer
     @action(detail=False,methods=['GET','POST'])    
     def todo_view_list(self,request):
         if request.method=='GET':
               task = Task.objects.filter(user_id=request.user.id)
               serializer = TaskSerializer(task,many=True)
               return Response(serializer.data)
         elif request.method=='POST':
               task = Task.objects.create(user_id=request.user.id)
               serializer = TaskSerializer(task, data=request.data)
               serializer.is_valid(raise_exception=True)
               serializer.save()
               return Response(serializer.data)


# @api_view(['GET','DELETE'])    
# def todo_view_dataile(request,id1,id2):
#     result=Task.objects.filter(user_id=id1).get(pk=id2)
#     if request.method=='GET':   
#              serializer=TaskSerializer(result)
#              return Response(serializer.data)
#     elif request.method=='DELETE':
#             result.delete()
#             return Response("ok")
    
              
        

     




   
 
    
    

        
