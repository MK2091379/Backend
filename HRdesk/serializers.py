from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from Register.models import User,Company
from djoser.serializers import UserSerializer as BaseUserSerializer


class HRdeskSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields=['username','first_name','last_name',
                  'email','role','company','birthdate',
                  'personal_id','father_full_name','mother_full_name',
                  'address','postal_code','sexuality','telephone',
                  'maritalـstatus','degreeـofـeducation']