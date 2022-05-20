from django import views
from django.urls import path 
from . import views



urlpatterns = [
    
    
    path('note/',views.FileView.as_view({'post':'note_view'})),
]
