from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from urllib import request, response
from TimeAndDateTracker.apps import TimeanddatetrackerConfig
from .models import TimeAndDateTracker
from .serializers import TimeAndDateTrackerSerializer,TimeAndDateTrackerUpdatingSerializer
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination






class TimeAndDateTrackerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TimeAndDateTracker.objects.all()
    serializer_class = TimeAndDateTrackerSerializer
    pagination_class=PageNumberPagination
    @action(detail=False, methods=['GET','POST'])
    def me(self, request):
        if request.method == 'GET':
            paginator=PageNumberPagination()
            paginator.page_size=8
            tracker = paginator.paginate_queryset(TimeAndDateTracker.objects.filter(user_id=request.user.id),request)
            serializer = TimeAndDateTrackerSerializer(tracker,many=True)
            return paginator.get_paginated_response(serializer.data)
        
        elif request.method == 'POST':
            tracker = TimeAndDateTracker.objects.create(user_id=request.user.id)
            serializer = TimeAndDateTrackerSerializer(tracker, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

class TimeAndDateTrackerUpdatingSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TimeAndDateTracker.objects.all()
    serializer_class = TimeAndDateTrackerUpdatingSerializer
    @action(detail=False, methods=['PUT'])
    def me(self, request):
        if request.method == 'PUT':
            tracker = TimeAndDateTracker.objects.get(user_id=request.user.id,id=request.data["id"])
            serializer = TimeAndDateTrackerUpdatingSerializer(tracker, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)                
        
#{
#  "date": "2022-04-16",
#  "start_point": null,
#  "end_point": null,
#  "wasted_time": 0
#}