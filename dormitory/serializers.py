from rest_framework import serializers
from Register.models import Company,User
from .models import Dormitory

class FoodSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Dormitory
        fields = ['user_id','id', 'number', 'capacity','company']