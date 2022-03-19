from urllib import request
from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Employee,CompanyOwner
from .serializers import CompanyOwnerSerializer, EmployeeSerializer,CompanyOwnerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404



#class EmployeeView(generics.ListCreateAPIView):
#
#    queryset=Employee.objects.all()
#    serializer_class=EmployeeSerializer
#    permissions.IsAuthenticatedOrReadOnly

# @api_view(['GET'])
# def ApiOverview_E(request):
#     api_urls = {
#         'all_items': '/',
#         'Search by Category': '/?category=category_name',
#         'Search by Subcategory': '/?subcategory=category_name',
#         'Add': '/create',
#         'Update': '/update/pk',
#         'Delete': '/item/pk/delete'
#     }
  
#     return Response(api_urls)
# @api_view(['POST'])
# def add_items_E(request):
#     item = EmployeeSerializer(data=request.data)
  
#     if Employee.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')
  
#     if item.is_valid():
#         item.save()
#         return Response(item.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
# @api_view(['GET'])
# def view_items_E(request):
# 	if request.query_params:
# 		items = Employee.objects.filter(**request.query_param.dict())
# 	else:
# 		items = Employee.objects.all()
# 	if items:
# 		data = EmployeeSerializer(items)
# 		return Response(data)
# 	else:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
# @api_view(['POST'])
# def update_items_E(request, pk):
# 	item = Employee.objects.get(pk=pk)
# 	data = EmployeeSerializer(instance=item, data=request.data)

# 	if data.is_valid():
# 		data.save()
# 		return Response(data.data)
# 	else:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
# @api_view(['DELETE'])
# def delete_items_E(request, pk):
# 	item = get_object_or_404(Employee, pk=pk)
# 	item.delete()
# 	return Response(status=status.HTTP_202_ACCEPTED)







# @api_view(['GET'])
# def ApiOverview_C(request):
#     api_urls = {
#         'all_items': '/',
#         'Search by Category': '/?category=category_name',
#         'Search by Subcategory': '/?subcategory=category_name',
#         'Add': '/create',
#         'Update': '/update/pk',
#         'Delete': '/item/pk/delete'
#     }
  
#     return Response(api_urls)
# @api_view(['POST'])
# def add_items_C(request):
#     item = CompanyOwner(data=request.data)
#     if CompanyOwner.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')
  
#     if item.is_valid():
#         item.save()
#         return Response(item.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)
# @api_view(['GET'])
# def view_items_C(request):
# 	if request.query_params:
# 		items = CompanyOwner.objects.filter(**request.query_param.dict())
# 	else:
# 		items = CompanyOwner.objects.all()
# 	if items:
# 		data = CompanyOwnerSerializer(items)
# 		return Response(data)
# 	else:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
# @api_view(['POST'])
# def update_items_C(request, pk):
# 	item = CompanyOwner.objects.get(pk=pk)
# 	data = CompanyOwnerSerializer(instance=item, data=request.data)

# 	if data.is_valid():
# 		data.save()
# 		return Response(data.data)
# 	else:
# 		return Response(status=status.HTTP_404_NOT_FOUND)
# @api_view(['DELETE'])
# def delete_items_C(request, pk):
# 	item = get_object_or_404(CompanyOwner, pk=pk)
# 	item.delete()
# 	return Response(status=status.HTTP_202_ACCEPTED)












