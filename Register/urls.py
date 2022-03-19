from django.urls import path,include
from . import views



urlpatterns=[
    path('employee/signup/',views.CreateEmployeeView.as_view()),
    path('company-owner/signup/',views. CompanyOwnerView.as_view()),
]