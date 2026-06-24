from rest_framework.routers import DefaultRouter
from django.urls import path, include # Asegúrate de tener estas importaciones

from .views import (
    CargoEmpleadoViewSet,
    TurnoViewSet,
    EmpleadoViewSet,
    EmpleadoTurnoViewSet
)

router = DefaultRouter()

router.register('cargos', CargoEmpleadoViewSet)
router.register('turnos', TurnoViewSet)
# Cambiamos 'empleados' por '' para que responda directo en /api/empleados/
router.register('', EmpleadoViewSet, basename='empleado') 
router.register('empleado-turnos', EmpleadoTurnoViewSet)

# Envolvemos las urls en un include() para que Django las lea bien
urlpatterns = [
    path('', include(router.urls)),
]