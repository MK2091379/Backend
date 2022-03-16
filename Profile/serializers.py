from dataclasses import field
from rest_framework import serializers
from .models import User,Company

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','email','phone','company','role']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=['company_name','company_biography']
