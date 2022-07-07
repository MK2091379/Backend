from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from urllib import request, response
from .models import BulletinBoard
from .serializers import BulletinBoardSerializer
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import  PageNumberPagination


paginator=PageNumberPagination()
paginator.page_size=8

class BulletinBoardViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BulletinBoard.objects.all()
    serializer_class = BulletinBoardSerializer
    
    @action(detail=False, methods=['GET'])
    def get_bulletin_board(self, request):
        if request.method == 'GET':
            queryset = paginator.paginate_queryset(BulletinBoard.objects.all(),request)
            serializer = BulletinBoardSerializer(queryset,many=True)
            return paginator.get_paginated_response(serializer.data)
        
    @action(detail=False, methods=['POST'])
    def post_bulletin_board(self, request):
        if request.method == 'POST':
            query = BulletinBoard.objects.create()
            serializer = BulletinBoardSerializer(query, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)