from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination 
import ToDoList
from .models import Task
from .serializers import TaskSerializer
from ToDoList import serializers






# Create your views here.

class ToDoListViewSet(ModelViewSet):
     permission_classes = [IsAuthenticated]
     serializer_class=TaskSerializer
     pagination_class=PageNumberPagination
     @action(detail=False,methods=['GET','POST'])    
     def todo_view_list(self,request):
         if request.method=='GET':
               paginator=PageNumberPagination()
               paginator.page_size=10
               queryset = paginator.paginate_queryset(
                     Task.objects.filter(user_id=request.user.id).order_by('priority'),
                                                      request)
               serializer = TaskSerializer(queryset,many=True)
               return paginator.get_paginated_response(serializer.data)
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
    
              
        

     




   
 
    
    

        
