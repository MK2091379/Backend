from dataclasses import field
from rest_framework import serializers
from .models import Employee,CompanyOwner

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="_all_"


class CompanyOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyOwner
        fields="_all_"