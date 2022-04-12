from django.urls import path#,include,re_path
from . import views



urlpatterns=[
    path('employee/',views.submit_date_and_time)
]