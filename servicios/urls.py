from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipoHabitacionServicioViewSet

router = DefaultRouter()

router.register(
    r'tipos-habitacion-servicios',
    TipoHabitacionServicioViewSet,
    basename='tipos-habitacion-servicios'
)

urlpatterns = [
    path('', include(router.urls)),
]