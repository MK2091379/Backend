from django.urls import path , include 
from . import views
from rest_framework_nested import routers



router = routers.DefaultRouter()
router.register('mytodolist', views.ToDoListViewSet)
urlpatterns = router.urls

    
#     path('mytodolist/',views.ToDoListViewSet.as_view()),
#     path('mytodolist/<int:id1>/<int:id2>',views.todo_view_dataile),
    
# ]