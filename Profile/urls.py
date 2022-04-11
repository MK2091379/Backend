from django.urls import path
from . import views
from rest_framework_nested import routers

#urlpatterns = [
#	#path('createE/', views.add_items_E, name='add-items-E'),
#	#path('viewE/', views.view_items_E, name='view-items-E'),
#	#path('updateE/<int:pk>/', views.update_items_E, name='update_items-E'),
#	#path('item/<int:pk>/deleteE/', views.delete_items_E, name='delete_items-E'),
#  	#path('createC/', views.add_items_C, name='add-items-C'),
#	#path('viewC/', views.view_items_C, name='view-items-C'),
#	#path('updateC/<int:pk>/', views.update_items_C, name='update_items-C'),
#	#path('item/<int:pk>/deleteC/', views.delete_items_C, name='delete_items-C'),
#]
router = routers.DefaultRouter()
router.register('employee', views.EmployeeViewSet)
#router.register('deleteE', views.EmployeeViewSet)
urlpatterns = router.urls