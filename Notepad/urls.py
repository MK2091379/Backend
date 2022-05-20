from django import views
from django.urls import path 
from . import views



urlpatterns = [
    
    
    path('note/',views.AddFileView.as_view()),
]
