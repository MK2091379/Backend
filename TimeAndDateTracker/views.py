from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from urllib import request, response
from TimeAndDateTracker.apps import TimeanddatetrackerConfig
from .models import TimeAndDateTracker
from .serializers import TimeAndDateTrackerSerializer
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import viewsets



class TimeAndDateTrackerViewSet(ModelViewSet):
    queryset = TimeAndDateTracker.objects.all()
    serializer_class = TimeAndDateTrackerSerializer
    @action(detail=False, methods=['GET','PUT'])
    def me(self, request):
        tracker = TimeAndDateTracker.objects.get(pk=1)
        #if request.method == 'GET':
        #    serializer = TimeAndDateTrackerSerializer(tracker)
        #    return Response(serializer.data)
        #elif request.method == 'PUT':
        #    serializer = TimeAndDateTrackerSerializer(tracker, data=request.data)
        #    serializer.is_valid(raise_exception=True)
        #    serializer.save()
        #    return Response(serializer.data)
        return Response(tracker)