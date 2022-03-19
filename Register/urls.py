from django.urls import path,include,re_path
from . import views









urlpatterns=[
    path('employee/signup/',views.CreateEmployeeView.as_view()),
    path('company-owner/signup/',views. CompanyOwnerView.as_view()),
    
    
   
   
]