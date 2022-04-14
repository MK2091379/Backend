from dataclasses import fields
from datetime import date
from pyexpat import model
from rest_framework import serializers
from .models import TimeAndDateTracker

class TimeAndDateTrackerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = TimeAndDateTracker
        fields = ['date', 'start_point', 'end_point', 'wasted_time', 'user_id']