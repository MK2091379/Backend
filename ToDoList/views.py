from django.shortcuts import get_object_or_404

import ToDoList
from .models import Task
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from .serializers import TaskSerializer
from ToDoList import serializers
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class ToDoListViewSet(ModelViewSet):
     permission_classes = [IsAuthenticated]
     serializer_class=TaskSerializer
     @action(detail=False,methods=['GET','POST'])    
     def todo_view_list(self,request):
         if request.method=='GET':
               queryset = Task.objects.filter(user_id=request.user.id).order_by('priority')
               serializer = TaskSerializer(queryset,many=True)
               return Response(serializer.data)
         elif request.method=='POST':
               task = Task.objects.create(user_id=request.user.id)
               serializer = TaskSerializer(task, data=request.data)
               serializer.is_valid(raise_exception=True)
               serializer.save()
               return Response(serializer.data)
class TaskUpdatingSet(ModelViewSet):
      
    serializer_class=TaskSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['PUT','DELETE'])
    def taskupdate (self, request,id1):
          task = get_object_or_404(Task,user_id=request.user.id,id=id1)
          if request.method == 'PUT':
               task = get_object_or_404(Task,user_id=request.user.id,id=id1)
               serializer = TaskSerializer(task, data=request.data)
               serializer.is_valid(raise_exception=True)
               serializer.save()
               return Response(serializer.data,status=status.HTTP_200_OK)
          elif request.method == 'DELETE':
                task.delete()
                return Response(status=status.HTTP_200_OK)
    
              
        

     




   
 
    
    

        
