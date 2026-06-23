from django.db import models


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nombre