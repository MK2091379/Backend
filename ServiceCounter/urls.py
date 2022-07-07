from django.urls import path
from . import views


urlpatterns = [
                    path("sendrequest/",views.EmployeeServiceCounter.as_view({'get':'send_reuqest','post':'send_reuqest'})),
                    path("sendresponse/",views.AdminServiceCounter.as_view({'get':'response_me'})),
                    path("sendresponse/<int:id>",views.AdminServiceCounter.as_view({'patch':'__show_all_request__'})),
]
