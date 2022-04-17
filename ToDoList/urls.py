from django.urls import path , include 
from . import views


urlpatterns=[
    
    path('mytodolist/<int:id>/',views.todo_view_list),
    path('mytodolist/<int:id1>/<int:id2>',views.todo_view_dataile),
    
]