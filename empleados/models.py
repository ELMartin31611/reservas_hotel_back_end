from django.db import models
from django.contrib.auth.models import User


class CargoEmpleado(models.Model):

    nombre = models.CharField(max_length=80)

    descripcion = models.TextField(
        blank=True,
        null=True
    )

    nivel_acceso = models.IntegerField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cargo_empleado'


class Turno(models.Model):

    nombre = models.CharField(max_length=50)

    hora_inicio = models.TimeField()

    hora_fin = models.TimeField()

    descripcion = models.TextField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'turno'


class Empleado(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='empleados'
    )

    cargo = models.ForeignKey(
        CargoEmpleado,
        on_delete=models.CASCADE,
        related_name='empleados'
    )

    hotel_id = models.BigIntegerField()

    cedula = models.CharField(
        max_length=20,
        unique=True
    )

    nombres = models.CharField(
        max_length=100
    )

    apellidos = models.CharField(
        max_length=100
    )

    telefono = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    fecha_contratacion = models.DateField(
        blank=True,
        null=True
    )

    salario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    estado = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        db_table = 'empleado'


class EmpleadoTurno(models.Model):

    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        related_name='turnos_asignados'
    )

    turno = models.ForeignKey(
        Turno,
        on_delete=models.CASCADE,
        related_name='empleados_asignados'
    )

    dia_semana = models.CharField(
        max_length=20
    )

    fecha_inicio = models.DateField()

    fecha_fin = models.DateField(
        blank=True,
        null=True
    )

    activo = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.empleado} - {self.turno}"

    class Meta:
        db_table = 'empleado_turno'