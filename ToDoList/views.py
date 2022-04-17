from django.shortcuts import get_object_or_404

import ToDoList
from .models import Task
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from .serializers import TaskSerializer,TaskUpdatingSerializer
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
class TaskUpdatingSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskUpdatingSerializer
    @action(detail=False, methods=['PUT'])
    def me(self, request):
          if request.method == 'PUT':
               task = Task.objects.get(user_id=request.user.id,id=request.data["id"])
               serializer = TaskUpdatingSerializer(task, data=request.data)
               serializer.is_valid(raise_exception=True)
               serializer.save()
               return Response(serializer.data)
    
              
        

     




   
 
    
    

        
