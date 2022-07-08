from django.urls import path
from . import views



urlpatterns=[
    path('get_company_assets',views.CompanyAssetsViewSet.as_view({'get':'get_company_assets'})),
    path('post_company_assets',views.CompanyAssetsViewSet.as_view({'post':'post_company_assets'})),
    path('put_company_assets/<int:id>',views.CompanyAssetsViewSet.as_view({'put':'put_company_assets'})),
    path('delete_company_assets/<int:id>',views.CompanyAssetsViewSet.as_view({'delete':'delete_company_assets'})),
]