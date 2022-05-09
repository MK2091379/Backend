from rest_framework import serializers
from .models import BulletinBoard

class TimeAndDateTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletinBoard
        fields = ['html_fields']
