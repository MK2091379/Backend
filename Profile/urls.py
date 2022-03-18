from django.urls import path
from . import views

urlpatterns = [
	path('E', views.ApiOverview_E, name='home'),
 	path('C', views.ApiOverview_E, name='home'),
  	#path('createE/',views.EmployeeView.as_view()),
	path('createE/', views.add_items_E, name='add-items-E'),
	path('viewE/', views.view_items_E, name='view-items-E'),
	path('updateE/<int:pk>/', views.update_items_E, name='update_items-E'),
	path('item/<int:pk>/deleteE/', views.delete_items_E, name='delete_items-E'),
 	#path('createC/',views.EmployeeView.as_view()),
  	path('createC/', views.add_items_C, name='add-items-C'),
	path('viewC/', views.view_items_C, name='view-items-C'),
	path('updateC/<int:pk>/', views.update_items_C, name='update_items-C'),
	path('item/<int:pk>/deleteC/', views.delete_items_C, name='delete_items-C'),
]
