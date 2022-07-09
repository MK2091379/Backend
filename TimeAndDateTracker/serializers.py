from rest_framework import serializers
from .models import TimeAndDateTracker

class TimeAndDateTrackerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = TimeAndDateTracker
        fields = ['id','created_date', 'start_point', 'end_point', 'wasted_time', 'user_id']
class TimeAndDateTrackerUpdatingSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only = False)
    class Meta:
        model = TimeAndDateTracker
        fields = ['id','created_date', 'start_point', 'end_point', 'wasted_time', 'user_id']
