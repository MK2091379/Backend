from rest_framework import serializers
from Register.models import User
from .models import CompanyAssets

class CompanyAssetsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = CompanyAssets
        fields = ['user','id', 'name','description','number']
        read_only_fields = ['user']