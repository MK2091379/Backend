from dataclasses import field
from rest_framework import serializers
from .models import User,Company

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','phone','email','company']


class CompnyOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','phone','email']
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=['company_name','company_biography']

