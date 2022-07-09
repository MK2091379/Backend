from django.urls import path#,include,re_path
from rest_framework_nested import routers
from . import views



router = routers.DefaultRouter()
router.register('', views.TimeAndDateTrackerViewSet)
router.register('update', views.TimeAndDateTrackerUpdatingSet)
urlpatterns = router.urls