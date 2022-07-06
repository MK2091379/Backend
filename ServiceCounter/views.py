
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from ServiceCounter.serializers import *
from .models import *
from automation.pagination import defult8_pagination
class AdminServiceCounter(ModelViewSet):
    serializer_class=ResponseSerializer
    
    queryset=RequestForm.objects.all()
    
    
    action(detail=False ,methods=['GET'])
    def response_me(self ,request):
            listrequest=RequestForm.objects.filter(user__company=request.user.company,status='P',user__role='E').order_by('created_time')
            serlializers=ResponseSerializer(listrequest,many=True)
            return Response(serlializers.data)
        
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
            listrequest=RequestForm.objects.filter(user_id=request.user.id)
            serlializers=ResponseSerializer(listrequest,many=True)
            return Response(serlializers.data)
   
            
            


