from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ReleveViewSet

router = DefaultRouter()
router.register('releves', ReleveViewSet, basename='releves')

urlpatterns = [
    path('', include(router.urls))
]