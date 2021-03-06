from django.conf.urls import url, include
from .views import GPSTimeViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('GPS', GPSTimeViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]