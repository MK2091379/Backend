from django.urls import path,include
from . import views



urlpatterns=[
    path('employee/',views.CreateEmployeeView.as_view()),
    path('company-owner/',views.CreateCompanyOwnerView.as_view()),
    path('company-owner/company',views.CreateCompanyView.as_view())
    
]