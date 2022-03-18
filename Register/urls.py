from django.urls import path,include
from . import views



urlpatterns=[
    path('employee/',views.CreateEmployeeView.as_view()),
    path('company-owner/',views. CompanyOwnerView.as_view()),

]