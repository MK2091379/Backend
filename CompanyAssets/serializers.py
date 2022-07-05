from rest_framework import serializers
from Register.models import User
from .models import CompanyAssets

class CompanyAssetsSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = CompanyAssets
        fields = ['user_id','id', 'name','description','number']