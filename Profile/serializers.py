from dataclasses import field
from email.mime import image
from django.conf import settings
from rest_framework import serializers
from django.conf import settings
from Register.models import Company, User
from .models import Employee,CompanyOwner
class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
class CompanyOwnerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyOwner
        fields = "__all__"