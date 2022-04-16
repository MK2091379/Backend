from django.urls import path , include 
from . import views


urlpatterns=[
    
    path('showmytodo/<int:id>/',views.todo_view),
    
]