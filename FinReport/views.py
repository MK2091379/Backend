from urllib import response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from automation.permissions import IsCompanyOwner 
from rest_framework.pagination import PageNumberPagination
from .serializers import AddReportSerializer,EditReportSerializer
from rest_framework.response import Response
from rest_framework import status
from FinReport.models import Report
from .serializers import AddReportSerializer,EditReportSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class ReportDetail(ModelViewSet):
    
    serializer_class=AddReportSerializer
    queryset=Report.objects.all()
    pagination_class=PageNumberPagination
    permission_classes=[IsAuthenticated,IsCompanyOwner]
    
    @action(detail=False,methods=['POST'])
    def post_report(self,request):
        new_report=Report(admin_id=request.user.id)
        serializer=AddReportSerializer(new_report,data=request.data)
        serializer.is_valid(raise_exception=True)
        new_report.save()
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @action(detail=False,methods=['GET'])
    def get_report(self,request):
        paginator=PageNumberPagination()
        paginator.page_size=10
        listreport=paginator.paginate_queryset(Report.objects.filter(admin_id=request.user.id),request)
        serializer=AddReportSerializer(listreport,many=True)
        return paginator.get_paginated_response(serializer.data)



class ActionReport(ModelViewSet):
    
    serializer_class=EditReportSerializer
    queryset=Report.objects.all()
    permission_classes=[IsAuthenticated,IsCompanyOwner]
    
    @action(detail=False,methods=['PATCH','DELETE'])
    def edit_delete_form(self,request,id):
        
        get_report=get_object_or_404(Report,pk=id,admin_id=self.request.id)
        if request.method=='PATCH':
            serializer=EditReportSerializer(get_report,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        
        elif request.method=='DELETE':
            get_report.delete()
            return response(status=status.HTTP_200_OK)
        
        
            
    
    