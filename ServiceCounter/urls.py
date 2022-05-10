from django.urls import path
from . import views





urlpatterns = [

    
    path('admintransportations/',views.AdminTransportationViewSet.as_view({'get':'admin_transportation_view_list','post':'admin_transportation_view_list'})),
    path('admintransportations/service/<int:id1>',views.ServiceUpdatingSet.as_view({'put':'serviceupdate','delete':'serviceupdate'})),
    path('admintransportations/checkrequests/',views.Get_Request_Admin_ViewSet.as_view({'get':'request_admin_view_list'})),
    
    path('request/new/',views.RequestViewSet.as_view({'post':'request_view_list'})),
    path('request/myrequests/',views.RequestViewSet.as_view({'get':'request_view_list'})),
    
]