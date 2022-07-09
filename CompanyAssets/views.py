from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from urllib import request, response
from .models import CompanyAssets
from .serializers import CompanyAssetsSerializer
# Create your views here.


class CompanyAssetsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CompanyAssets.objects.all()
    serializer_class = CompanyAssetsSerializer
    @action(detail=False, methods=['GET'])
    def get_company_assets(self, request):
        if request.method == 'GET':
            company_assets = CompanyAssets.objects.filter(user_id = request.user.id)
            serializer = CompanyAssetsSerializer(company_assets,many=True)
            return Response(serializer.data)
    @action(detail=False, methods=['POST'])
    def post_company_assets(self,request):
        if request.method == 'POST':
            company_assets = CompanyAssets.objects.create(user_id = request.user.id)
            serializer = CompanyAssetsSerializer(company_assets, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    @action(detail=False, methods=['PUT'])
    def put_company_assets(self,request,id):
        if request.method == 'PUT':
            company_assets = CompanyAssets.objects.get(id=id)
            serializer = CompanyAssetsSerializer(company_assets, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    @action(detail=False, methods=['DELETE'])
    def delete_company_assets(self,request,id):
        if request.method == 'DELETE':
            CompanyAssets.objects.get(id=id).delete()
            return Response("OK")