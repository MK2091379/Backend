from django.urls import path
from . import views



urlpatterns=[
    path('get_dormitory_manager',views.DormitoryViewSetManager.as_view({'get':'get_dormitory_manager'})),
    path('post_dormitory',views.DormitoryViewSetManager.as_view({'post':'post_dormitory'})),
    path('put_dormitory/<str:number>',views.DormitoryViewSetManager.as_view({'put':'put_dormitory'})),
    path('delete_dormitory/<str:number>',views.DormitoryViewSetManager.as_view({'delete':'delete_dormitory'})),
    ###########################################################################################################################
    #path('get_reserved_dormitory_manager',views.dormitoryViewSetManager.as_view({'get':'get_reserved_dormitory_manager'})),
    path('reserve_dormitory_manager/<str:number>/<str:company>',views.DormitoryViewSetManager.as_view({'get':'reserve_dormitory_manager'})),
    path('delete_reserved_dormitory_manager/<str:number>/<str:company>/<str:date>',views.DormitoryViewSetManager.as_view({'get':'delete_reserved_dormitory_manager'})),
    #######################################################################################################################
    #path('get_reserved_dormitory_employee',views.dormitoryViewSetEmployee.as_view({'get':'get_reserved_dormitory_employee'})),
    path('reserve_dormitory_employee/<str:number>/<str:company>/<str:date>',views.DormitoryViewSetEmployee.as_view({'get':'reserve_dormitory_employee'})),
    path('delete_reserved_dormitory_employee/<str:number>/<str:company>/<str:date>',views.DormitoryViewSetEmployee.as_view({'get':'delete_reserved_dormitory_employee'})),
]