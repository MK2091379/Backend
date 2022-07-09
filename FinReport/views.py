from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from automation.permissions import IsCompanyOwner 
from .serializers import AddReportSerializer,EditReportSerializer,MinInfoSerializer
from .serializers import AddReportSerializer,EditReportSerializer
from FinReport.models import Report

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
        
        get_report=get_object_or_404(Report,pk=id,admin_id=self.request.user.id)
        if request.method=='PATCH':
            serializer=EditReportSerializer(get_report,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        
        elif request.method=='DELETE':
            get_report.delete()
            return Response(status=status.HTTP_200_OK)


class ChartReport(ModelViewSet):
    
    serializer_class=MinInfoSerializer
    queryset=Report.objects.all()
    permission_classes=[IsAuthenticated,IsCompanyOwner]
    
    
    @action (detail=False,methods=['GET'])
    def get_limited_info(self,request,Sdate,Edate):
     Listmininforeport=Report.objects.filter(date_period__gt=Sdate,date_period__lt=Edate,admin_id=request.user.id)
     serializer=MinInfoSerializer(Listmininforeport,many=True)
     return  Response(serializer.data,status=status.HTTP_200_OK)
     
     
     
        
        
            
    
    