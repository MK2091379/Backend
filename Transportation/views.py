from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from Transportation import serializers
from Register.models import User
from automation.permissions import IsCompanyOwner, IsEmployee
from .serializers import AdminTransportationSerializer, EmployeeGetSerializer, UserTransportationSerializer
from .models import AdminTransportation
from automation.permissions import IsEmployee,IsCompanyOwner







class AdminTransportationViewSet(ModelViewSet):
     permission_classes = [IsAuthenticated, IsCompanyOwner]
     queryset = AdminTransportation.objects.all()
     serializer_class = AdminTransportationSerializer
     pagination_class=PageNumberPagination

     @action(detail=False, methods=['GET', 'POST'])
     def admin_transportation_view_list(self, request):
         if request.method == 'GET':
               paginator=PageNumberPagination()
               paginator.page_size=10
               queryset =paginator.paginate_queryset (AdminTransportation.objects.filter(
                   admin_id=request.user.id),request)
               serializer = AdminTransportationSerializer(queryset, many=True)
               
               return paginator.get_paginated_response(serializer.data)
         elif request.method == 'POST':
               location = AdminTransportation.objects.create(
                   admin_id=request.user.id, admin=request.user)
               serializer = AdminTransportationSerializer(
                   location, data=request.data)
               serializer.is_valid(raise_exception=True)
               serializer.save()
               return Response(serializer.data)


class ServiceUpdatingSet(ModelViewSet):

    serializer_class = AdminTransportationSerializer
    permission_classes = [IsAuthenticated, IsCompanyOwner]

    @action(detail=False, methods=['PUT', 'DELETE'])
    def serviceupdate(self, request, id1):
          service = get_object_or_404(
              AdminTransportation, admin_id=request.user.id, id=id1)
          if request.method == 'PUT':
            #    task = get_object_or_404(Task,user_id=request.user.id,id=id1)
               serializer = AdminTransportationSerializer(
                   service, data=request.data)
               serializer.is_valid(raise_exception=True)
               serializer.save()
               return Response(serializer.data, status=status.HTTP_200_OK)
          elif request.method == 'DELETE':
                service.delete()
                return Response(status=status.HTTP_200_OK)


class EmployeeReserve(ModelViewSet):

    permission_classes = [IsAuthenticated,IsEmployee]
    queryset = AdminTransportation.objects.all()
    serializer_class = EmployeeGetSerializer
    pagination_class=PageNumberPagination
    @action(detail=False, methods=['GET'])
    def getlist_view(self, request):
            paginator=PageNumberPagination()
            paginator.page_size=10
            queryset = paginator.paginate_queryset(AdminTransportation.objects.filter(
                admin__company=request.user.company),request)
            serializer = EmployeeGetSerializer(queryset, many=True)
            return paginator.get_paginated_response(serializer.data)

    @action(detail=False, methods=['PATCH'])
    def reserve_view(self, request, id):
        if request.method == 'PATCH':
            reserve = get_object_or_404(AdminTransportation, id=id)
            reserve.user.add(request.user.id)
            if reserve.maximum_capacity > 0:
                reserve.maximum_capacity -= 1
            else:
                return Response(status="Capacity is complete!")

            reserve.save()
            return Response(status=status.HTTP_200_OK)

    @action(detail=False,methods=['PATCH'])
    def unreserve_view(self,request,id):
        if request.method=='PATCH':
            reserve = get_object_or_404(AdminTransportation,id=id)
            reserve.user.remove(request.user.id)
            reserve.maximum_capacity+=1
                
            reserve.save()
            return Response(status=status.HTTP_200_OK)
    
    
class ShowServicesApi(ModelViewSet):
       serializer_class=UserTransportationSerializer
       permission_classes = [IsAuthenticated,IsEmployee]
       @action(detail=False,methods=['GET'])   
       def myservice_view(self,request):
         if request.method=='GET':
               user=get_object_or_404(User,id=request.user.id)
               serializer = UserTransportationSerializer(user)
               return Response(serializer.data)
            #    serializer = EmployeeGetSerializer(queryset,many=True)
