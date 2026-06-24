from rest_framework import viewsets

from .models import (
    CargoEmpleado,
    Turno,
    Empleado,
    EmpleadoTurno
)

from .serializers import (
    CargoEmpleadoSerializer,
    TurnoSerializer,
    EmpleadoSerializer,
    EmpleadoTurnoSerializer
)


class CargoEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = CargoEmpleado.objects.all()
    serializer_class = CargoEmpleadoSerializer


class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class EmpleadoTurnoViewSet(viewsets.ModelViewSet):
    queryset = EmpleadoTurno.objects.all()
    serializer_class = EmpleadoTurnoSerializer