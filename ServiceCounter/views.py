from django.shortcuts import get_object_or_404
from Register.models import User
from .models import AdminTransportation
from .serializers import AdminTransportationSerializer, EmployeeGetSerializer,UserTransportationSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response





from automation.permissions import IsCompanyOwner,IsEmployee

from ServiceCounter import serializers
# Create your views here.


class AdminTransportationViewSet(ModelViewSet):
     permission_classes = [IsAuthenticated,IsCompanyOwner]
     queryset = AdminTransportation.objects.all()
     serializer_class=AdminTransportationSerializer
     @action(detail=False,methods=['GET','POST'])    
     def admin_transportation_view_list(self,request):
         if request.method=='GET':
               queryset = AdminTransportation.objects.filter(admin_id=request.user.id)
               serializer = AdminTransportationSerializer(queryset,many=True)
               return Response(serializer.data)
         elif request.method=='POST':
               location = AdminTransportation.objects.create(admin_id=request.user.id,admin=request.user)
               serializer = AdminTransportationSerializer(location, data=request.data)
               serializer.is_valid(raise_exception=True)
               serializer.save()
               return Response(serializer.data)
           
class ServiceUpdatingSet(ModelViewSet):
      
    serializer_class=AdminTransportationSerializer
    permission_classes = [IsAuthenticated,IsCompanyOwner]

    @action(detail=False, methods=['PUT','DELETE'])
    def serviceupdate (self, request,id1):
          service = get_object_or_404(AdminTransportation,admin_id=request.user.id,id=id1)
          if request.method == 'PUT':
            #    task = get_object_or_404(Task,user_id=request.user.id,id=id1)
               serializer = AdminTransportationSerializer(service, data=request.data)
               serializer.is_valid(raise_exception=True)
               serializer.save()
               return Response(serializer.data,status=status.HTTP_200_OK)
          elif request.method == 'DELETE':
                service.delete()
                return Response(status=status.HTTP_200_OK)

class EmployeeReserve(ModelViewSet):
      
     permission_classes=[IsAuthenticated,IsEmployee]
     queryset =AdminTransportation.objects.all()
     serializer_class=EmployeeGetSerializer
     @action(detail=False,methods=['GET'])    
     def getlist_view(self,request):
               queryset = AdminTransportation.objects.filter(admin__company=request.user.company)
               serializer = EmployeeGetSerializer(queryset,many=True)
               return Response(serializer.data)
     @action(detail=False,methods=['PATCH'])   
     def reserve_view(self,request,id):
         if request.method=='PATCH':
               reserve = get_object_or_404(AdminTransportation,id=id)
               reserve.user.add(request.user.id)
               if reserve.maximum_capacity>0:
                   reserve.maximum_capacity-=1
               else:
                     return Response(status="Capacity is complete!")
            #    if int(reserve.user.get(request.user.id))!=None:
            #           return Response(status="waht the fuck")
                     
               reserve.save()
               return Response(status=status.HTTP_200_OK)
            #    serializer = EmployeeGetSerializer(queryset,many=True)
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
               
         
        
