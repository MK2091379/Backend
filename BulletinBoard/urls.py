from django.urls import path
from . import views



urlpatterns=[
    path('get_bulletin_board',views.BulletinBoardViewSet.as_view({'get':'get_bulletin_board'})),
    path('post_bulletin_board',views.BulletinBoardViewSet.as_view({'post':'post_bulletin_board'})),
]