from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import FormulaireViewSet, generate_pdf

router = DefaultRouter()
router.register("formulaires", FormulaireViewSet, basename="formulaires")

urlpatterns = [
    path('formulaires/<int:formulaire_id>/generate_pdf/', generate_pdf, name='generate_pdf'),
    path('', include(router.urls)),
]