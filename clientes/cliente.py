from django.db import models
from accounts.models import PerfilUsuario

class Cliente(models.Model):
    perfil = models.ForeignKey(
        PerfilUsuario,
        on_delete=models.CASCADE,
        related_name='clientes'
    )

    cedula = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    fecha_nacimiento = models.DateField(
        null=True,
        blank=True
    )

    genero = models.CharField(
        max_length=20,
        blank=True
    )

    nacionalidad = models.CharField(
        max_length=80,
        blank=True
    )

    correo_alternativo = models.EmailField(
        blank=True
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
        db_table = "cliente"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"