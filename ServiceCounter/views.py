
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from ServiceCounter.serializers import *
from .models import *






class AdminServiceCounter(ModelViewSet):
    serializer_class=ResponseSerializer
    queryset=RequestForm.objects.all()
    pagination_class=PageNumberPagination
    
    
    action(detail=False ,methods=['GET'])
    def response_me(self ,request):
        
            paginator=PageNumberPagination()
            paginator.page_size=8
            listrequest=paginator.paginate_queryset(RequestForm.objects.filter(user__company=request.user.company,status='pending',user__role='E').order_by('created_time'),request)
            serlializers=ResponseSerializer(listrequest,many=True)
            return paginator.get_paginated_response(serlializers.data)
        
    action(detail=False ,methods=['PATCH'])
    def __show_all_request__(self ,request,id):
            getrequest=get_object_or_404(RequestForm,pk=id,user__company=request.user.company)
            serializer = ResponseSerializer(getrequest, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
     
        
        
class EmployeeServiceCounter(ModelViewSet):
    
    serializer_class=RequestSerializer
    
    queryset=RequestForm.objects.all()
    pagination_class=PageNumberPagination
    
    
    
    action(detail=False,methods=['POST','GET'])
    def send_reuqest(self,request):
        
        if request.method=='POST':
            requestinstance=RequestForm(user_id=request.user.id)
            serializer = RequestSerializer(requestinstance, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            requestinstance.save()
            return Response(serializer.data)
        
        elif request.method=='GET':
            paginator=PageNumberPagination()
            paginator.page_size=1
            listrequest=paginator.paginate_queryset(RequestForm.objects.filter(user_id=request.user.id),request)
            serlializers=ResponseSerializer(listrequest,many=True)
            return paginator.get_paginated_response(serlializers.data)
   
            
            


