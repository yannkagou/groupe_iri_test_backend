from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import EvaluationViewSet

router = DefaultRouter()
router.register('evaluations', EvaluationViewSet, basename='evaluations')

urlpatterns = [
    path('', include(router.urls))
]
