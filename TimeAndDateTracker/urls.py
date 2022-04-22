from django.urls import path#,include,re_path
from . import views
from rest_framework_nested import routers



router = routers.DefaultRouter()
router.register('', views.TimeAndDateTrackerViewSet)
router.register('update', views.TimeAndDateTrackerUpdatingSet)
urlpatterns = router.urls