from django.urls import path
from . import views



urlpatterns=[
    path('get_food_manager',views.FoodViewSet.as_view({'get':'get_food_manager'})),
    path('post_food',views.FoodViewSet.as_view({'post':'post_food'})),
    path('put_food',views.FoodViewSet.as_view({'put':'put_food'})),
    path('delete_food/<str:name>',views.FoodViewSet.as_view({'delete':'delete_food'})),
]