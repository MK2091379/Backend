from django.urls import path
from . import views


urlpatterns = [
    path('admin/',views.AdminTransportationViewSet.as_view({'get':'admin_transportation_view_list','post':'admin_transportation_view_list'})),
    path('admin/service/<int:id1>',views.ServiceUpdatingSet.as_view({'put':'serviceupdate','delete':'serviceupdate'})),
    path('employee/showlists',views.EmployeeReserve.as_view({'get':'getlist_view'})),
    path('employee/showlists/reserve/<int:id>',views.EmployeeReserve.as_view({'patch':'reserve_view'})),
    path('employee/showlists/unreserve/<int:id>',views.EmployeeReserve.as_view({'patch':'unreserve_view'})),
    path('employee/showmyservice/',views.ShowServicesApi.as_view({'get':'myservice_view'})),
]
