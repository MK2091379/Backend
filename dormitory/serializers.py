from dataclasses import fields
from rest_framework import serializers
from Register.models import Company,User
from .models import Dormitory


class UserRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name']
class DormitorySerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only = True)
    user_room = UserRoomSerializer(many = True)
    class Meta:
        model = Dormitory
        fields = ['user_id','id', 'number','building_name','remaining_capacity','user_room']