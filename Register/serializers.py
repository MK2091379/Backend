from dataclasses import field
from statistics import mode
from rest_framework import serializers
from .models import User,Company
from djoser.serializers import UserSerializer as BaseUserSerializer


class GetRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['role']
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=['company_name','company_biography']


class EmployeeSerializer(serializers.ModelSerializer):
    role=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','company','role']
    
    def create(self, validated_data):
        user = User.objects.create(
           
            
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            company=validated_data['company'],
            role='E'
        )

        
        user.set_password(validated_data['password'])
        user.save()
        return user
        

class EmployeeBaseSerializer(BaseUserSerializer):
     class Meta(BaseUserSerializer.Meta):
          fields=['username','first_name','last_name',
                  'email','role','company','birthdate',
                  'personal_id','father_full_name','mother_full_name',
                  'address','postal_code','sexuality','telephone',
                  'maritalـstatus','degreeـofـeducation']
    
    
class CompnyOwnerSerializer(serializers.ModelSerializer):
    role=serializers.CharField(read_only=True)
    company=CompanySerializer()
    
    class Meta:
        model=User
        fields=['company','first_name','last_name','username','email','role']
        
        
        
    def create(self, validated_data):                                                       
           
            company_data=validated_data.pop('company')
            company=CompanySerializer.create(CompanySerializer(),validated_data=company_data)
            company_owner,created=User.objects.update_or_create(company=company,
            first_name=validated_data.pop('first_name'),
            last_name=validated_data.pop('last_name'), 
            username=validated_data.pop('username'), 
            email=validated_data.pop('email'),
            role='C' 
            
            )
            company_owner.set_password(validated_data['password'])
            company_owner.save()
            return company_owner
            
            
            
            
            #  first_name=validated_data['first_name'],
            #  last_name=validated_data['last_name'],
            #  phone=validated_data['phone'],
            #  email=validated_data['email'],
            #  role='C' 
            
class CompanyGetSerializer(serializers.ModelSerializer):
        class Meta:
            model=Company
            fields=['company_name']
