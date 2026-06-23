from django.db import models


class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    sitio_web = models.URLField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class DireccionHotel(models.Model):
    hotel = models.OneToOneField(
        Hotel,
        on_delete=models.CASCADE,
        related_name="direccion"
    )

    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    referencia = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.hotel.nombre} - {self.ciudad}"