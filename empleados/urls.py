from rest_framework.routers import DefaultRouter

from .views import (
    CargoEmpleadoViewSet,
    TurnoViewSet,
    EmpleadoViewSet,
    EmpleadoTurnoViewSet
)

router = DefaultRouter()

router.register('cargos', CargoEmpleadoViewSet)
router.register('turnos', TurnoViewSet)
router.register('empleados', EmpleadoViewSet)
router.register('empleado-turnos', EmpleadoTurnoViewSet)

urlpatterns = router.urls