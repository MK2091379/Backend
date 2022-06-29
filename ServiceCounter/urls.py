from django.urls import path
from . import views


urlpatterns = [
                    path("sendrequest/",views.EmployeeServiceCounter.as_view({'get':'send_reuqest','post':'send_reuqest'})),
                    path("sendresponse/",views.AdminServiceCounter.as_view({'get':'response_and_show','patch':'response_and_show'}))
]
