from django.urls import path, include
from .views import MovieVS
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('movie', MovieVS, basename='movie')

urlpatterns = [
    path("", include(router.urls)),
]