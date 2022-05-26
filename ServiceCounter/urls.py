from django.urls import path
from . import views





urlpatterns = [

    
    path('transportation/admintransportations/',views.AdminTransportationViewSet.as_view({'get':'admin_transportation_view_list','post':'admin_transportation_view_list'})),
    path('transportation/admintransportations/service/<int:id1>',views.ServiceUpdatingSet.as_view({'put':'serviceupdate','delete':'serviceupdate'})),
    path('transportation/employee/showlists',views.EmployeeReserve.as_view({'get':'getlist_view'})),
    path('transportation/employee/showlists/reserve/<int:id>',views.EmployeeReserve.as_view({'patch':'reserve_view'})),
    path('transportation/employee/showlists/unreserve/<int:id>',views.EmployeeReserve.as_view({'patch':'unreserve_view'})),
    path('transportation/employee/showmyservice/',views.ShowServicesApi.as_view({'get':'myservice_view'})),
    
]