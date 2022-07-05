from rest_framework import serializers
from Register.models import User
from .models import Assets

class DormitorySerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Assets
        fields = ['user_id','id', 'name','description','number']