from dataclasses import fields
from rest_framework import serializers
from Register.models import Company,User
from .models import Dormitory

class DormitorySerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Dormitory
        fields = ['user_id','id', 'number','building_name','remaining_capacity']