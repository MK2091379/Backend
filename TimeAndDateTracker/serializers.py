from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import TimeAndDateTracker

class TimeAndDateTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeAndDateTracker
        fields = '__all__'