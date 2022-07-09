from xml.dom.minidom import CharacterData
from django.urls import path
from . import views



urlpatterns = [
    path('main/',views.ReportDetail.as_view({'post':'post_report','get':'get_report'})),
    path('main/<int:id>',views.ActionReport.as_view({'patch':'edit_delete_form','delete':'edit_delete_form'})),
    path('main/cahrt/<str:Sdate>/<str:Edateix >',views.ChartReport.as_view({'get':'get_limited_info'}))
]
