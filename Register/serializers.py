from dataclasses import field
from rest_framework import serializers
from .models import User,Company

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','email','phone','company','role']
        model2=Company
        field2=['company_name','company_biography']
