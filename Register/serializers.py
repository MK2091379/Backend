from dataclasses import field
from email.policy import default
from rest_framework import serializers
from .models import User,Company

class EmployeeSerializer(serializers.ModelSerializer):
    role=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','phone','email','company','role','password']
    
    def create(self, validated_data):
        user = User.objects.create(
           
            
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            role='E'
        )

        
        user.set_password(validated_data['password'])
        user.save()
        return user
        


class CompnyOwnerSerializer(serializers.ModelSerializer):
    role=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','phone','email','role']
    def create(self, validated_data):
        user = User.objects.create(
           
            
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            email=validated_data['email'],
            role='C'
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=['company_name','company_biography']

