from django.db import models
from django.contrib.auth.models import User
from empleados.models import CargoEmpleado
from hoteles.models import Hotel

class Empleado(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    cargo = models.ForeignKey(
        CargoEmpleado,
        on_delete=models.PROTECT
    )

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE
    )

    cedula = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    fecha_contratacion = models.DateField()
    salario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estado = models.CharField(
        max_length=20,
        default='ACTIVO'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"