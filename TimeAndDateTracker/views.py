from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from urllib import request
from TimeAndDateTracker.apps import TimeanddatetrackerConfig
from .models import TimeAndDateTracker
from .serializers import TimeAndDateTrackerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


api_view(['POST'])
def submit_date_and_time(request):
    date_and_time = TimeAndDateTracker.objects.get(user_id=request.user.id)
    serializer = TimeAndDateTrackerSerializer(date_and_time, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)