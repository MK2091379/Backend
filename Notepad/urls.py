from django import views
from django.urls import path 
from . import views



urlpatterns = [
    
    
    path('note/',views.AddFileView.as_view()),
    path('note/showmynotes',views.FileQuery.as_view({'get':'show_my_notes'})),
    path('note/showmynotes/deletefile/<int:id>',views.FileQuery.as_view({'delete':'delete_file'})),
    path('note/deltenote/<int:id>',views.FileQuery.as_view({'delete':'delete_note'})),
    path('note/updatenote/<int:id>',views.FileQuery.as_view({'patch':'update_note'})),
]
