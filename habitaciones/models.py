from django.db import models
from hoteles.models import Hotel


class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    capacidad = models.PositiveIntegerField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Cama(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


class TipoHabitacionCama(models.Model):
    tipo_habitacion = models.ForeignKey(
        TipoHabitacion,
        on_delete=models.CASCADE
    )

    cama = models.ForeignKey(
        Cama,
        on_delete=models.CASCADE
    )

    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.tipo_habitacion} - {self.cama}"


class Habitacion(models.Model):

    ESTADOS = [
        ("DISPONIBLE", "Disponible"),
        ("OCUPADA", "Ocupada"),
        ("MANTENIMIENTO", "Mantenimiento"),
    ]

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name="habitaciones"
    )

    tipo = models.ForeignKey(
        TipoHabitacion,
        on_delete=models.CASCADE
    )

    numero = models.CharField(max_length=10)
    piso = models.PositiveIntegerField()

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="DISPONIBLE"
    )

    def __str__(self):
        return self.numero


class ImagenHabitacion(models.Model):
    habitacion = models.ForeignKey(
        Habitacion,
        on_delete=models.CASCADE,
        related_name="imagenes"
    )

    url_imagen = models.URLField()
    descripcion = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return self.url_imagen