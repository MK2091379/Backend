from dataclasses import fields
from rest_framework import serializers

from FinReport.models import Report


class AddReportSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Report
        fields=['id','admin','name','type_report','amount','period','date_period']
        editead_only_fields=['id','admin']
class EditReportSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Report
        fields=['admin','name''amount','date_period']
        read_only_fields=['admin']