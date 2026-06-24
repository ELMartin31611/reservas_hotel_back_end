from rest_framework import serializers
from .models import (
    CargoEmpleado,
    Turno,
    Empleado,
    EmpleadoTurno
)


class CargoEmpleadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CargoEmpleado
        fields = '__all__'


class TurnoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Turno
        fields = '__all__'


class EmpleadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleado
        fields = '__all__'


class EmpleadoTurnoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmpleadoTurno
        fields = '__all__'