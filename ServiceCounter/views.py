from django.shortcuts import get_object_or_404
from .models import AdminTransportation
from .serializers import AdminTransportationSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,action
from rest_framework.response import Response





from automation.permissions import IsCompanyOwner,IsEmployee
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