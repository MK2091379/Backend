from django.urls import path
from . import views



urlpatterns=[
    path('get_food_manager',views.FoodViewSetManager.as_view({'get':'get_food_manager'})),
    path('post_food',views.FoodViewSetManager.as_view({'post':'post_food'})),
    path('put_food/<int:id>',views.FoodViewSetManager.as_view({'put':'put_food'})),
    path('delete_food/<int:id>',views.FoodViewSetManager.as_view({'delete':'delete_food'})),
    ###########################################################################################################################
    path('reserve_food_manager/<int:id>',views.FoodViewSetManager.as_view({'get':'reserve_food_manager'})),
    path('delete_reserved_food_manager/<int:id>',views.FoodViewSetManager.as_view({'delete':'delete_reserved_food_manager'})),
    #######################################################################################################################
    path('get_company_food_employee',views.FoodViewSetEmployee.as_view({'get':'get_company_food_employee'})),
    path('reserve_food_employee/<int:id>',views.FoodViewSetEmployee.as_view({'get':'reserve_food_employee'})),
    path('delete_reserved_food_employee/<int:id>',views.FoodViewSetEmployee.as_view({'delete':'delete_reserved_food_employee'})),
]