from django.urls import path
from . import views



urlpatterns=[
    path('master-employee',views.HRDeskViewSet.as_view({'get':'get_master_employee'})),
    path('becholar-employee',views.HRDeskViewSet.as_view({'get':'get_becholar_employee'})),
    path('diploma-employee',views.HRDeskViewSet.as_view({'get':'get_diploma_employee'})),
    path('other-employee',views.HRDeskViewSet.as_view({'get':'get_other_employee'})),
]