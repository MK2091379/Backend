from django.urls import path
from . import views



urlpatterns=[
    path('get_food_manager',views.FoodViewSetManager.as_view({'get':'get_food_manager'})),
    path('post_food',views.FoodViewSetManager.as_view({'post':'post_food'})),
    path('put_food/<str:name>',views.FoodViewSetManager.as_view({'put':'put_food'})),
    path('delete_food/<str:name>',views.FoodViewSetManager.as_view({'delete':'delete_food'})),
    ###########################################################################################################################
    #path('get_reserved_food_manager',views.FoodViewSetManager.as_view({'get':'get_reserved_food_manager'})),
    path('reserve_food_manager/<str:name>/<str:company>/<str:date>',views.FoodViewSetManager.as_view({'get':'reserve_food_manager'})),
    path('delete_reserved_food_manager/<str:name>/<str:company>/<str:date>',views.FoodViewSetManager.as_view({'get':'delete_reserved_food_manager'})),
    #######################################################################################################################
    #path('get_reserved_food_employee',views.FoodViewSetEmployee.as_view({'get':'get_reserved_food_employee'})),
    path('reserve_food_employee/<str:name>/<str:company>/<str:date>',views.FoodViewSetEmployee.as_view({'get':'reserve_food_employee'})),
    path('delete_reserved_food_employee/<str:name>/<str:company>/<str:date>',views.FoodViewSetEmployee.as_view({'get':'delete_reserved_food_employee'})),
]