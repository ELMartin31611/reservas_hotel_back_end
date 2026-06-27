from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TemporadaViewSet, TarifaHabitacionViewSet

router = DefaultRouter()

router.register(r'temporadas', TemporadaViewSet, basename='temporadas')
router.register(r'tarifas-habitacion', TarifaHabitacionViewSet, basename='tarifas-habitacion')

urlpatterns = [
    path('', include(router.urls)),
]