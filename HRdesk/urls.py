from django.urls import path
from . import views



urlpatterns=[
    path('get_employee',views.HRDeskViewSet.as_view({'get':'get_employee'})),
]