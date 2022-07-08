from urllib.parse import urlparse
from django.urls import path
from . import views



urlpatterns = [
    path('main/',views.ReportDetail.as_view({'post':'post_report','get':'get_report'})),
    path('main/<int:id>',views.ActionReport.as_view({'patch':'edit_delete_form','delete':'edit_delete_form'}))
]
