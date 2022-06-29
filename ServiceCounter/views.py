
from rest_framework.decorators import action
from django.shortcuts import get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated
from ServiceCounter import serializers
from  ServiceCounter.serializers import *
from .models import *



class AdminServiceCounter(ModelViewSet):
    serializer_class=ResponseSerializer
    queryset=RequestForm.objects.all()
    
    
    action(detail=False ,methods=['GET','PATCH'])
    def response_and_show(self ,request,id):
        if request.method=='GET':
            listrequest=RequestForm.objects.filter(user_company=request.user.comoany,user_role='E',status='P')
            serlializers=ResponseSerializer(listrequest,Many=True)
            return Response(serlializers.data)
        elif request.method=="PATCH":
            getrequest=get_list_or_404(RequestForm,pk=id)
            serializer = RequestSerializer(getrequest, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
class EmployeeServiceCounter(ModelViewSet):
    
    serializer_class=RequestSerializer
    queryset=RequestForm.objects.all()
    
    
    action(detail=False,methods=['POST','GET'])
    def send_reuqest(self,request):
        
        if request.method=='POST':
            requestinstance=RequestForm(user_id=request.user_id)
            serializer = RequestSerializer(requestinstance, data=request.data)
            serializer.is_valid(raise_exception=True)
            requestinstance.save()
            serializer.save()
            return Response(serializer.data)
        elif request.method=='GET':
            listrequest=RequestForm.objects.filter(user_id=request.user_id)
            serlializers=ResponseSerializer(listrequest,Many=True)
            return Response(serlializers.data)
        
   
            
            


