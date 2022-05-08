from django.urls import path
from . import views





urlpatterns = [

    
    path('admintransportations/',views.AdminTransportationViewSet.as_view({'get':'admin_transportation_view_list','post':'admin_transportation_view_list'})),
    path('admintransportations/service/<int:id1>',views.ServiceUpdatingSet.as_view({'put':'serviceupdate','delete':'serviceupdate'})),
    
]