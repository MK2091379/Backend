from dataclasses import fields
from datetime import date
from pyexpat import model
from rest_framework import serializers

from Register.models import Company
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only = True)
    #company = serializers.CharField(read_only = True)
    class Meta:
        model = Food
        fields = ['user_id','id','date', 'name','description','image','amount','company','price']
