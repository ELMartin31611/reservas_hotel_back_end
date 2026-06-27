from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    ]

    codigo = models.CharField(max_length=30, unique=True)
    cliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.CASCADE,
        related_name='reservas'
    )
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    numero_noches = models.PositiveIntegerField(default=1)
    cantidad_adultos = models.PositiveIntegerField(default=1)
    cantidad_ninos = models.PositiveIntegerField(default=0)
    estado = models.CharField(
        max_length=30,
        choices=ESTADO_CHOICES,
        default='pendiente'
    )
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    impuestos = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    descuento = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    observaciones = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-created_at']

    def clean(self):
        if self.fecha_salida <= self.fecha_entrada:
            raise ValidationError(
                'La fecha de salida debe ser mayor que la fecha de entrada.'
            )

    def calcular_noches(self):
        return (self.fecha_salida - self.fecha_entrada).days

    def __str__(self):
        return self.codigo


class ReservaHabitacion(models.Model):
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    ]

    reserva = models.ForeignKey(
        Reserva,
        on_delete=models.CASCADE,
        related_name='habitaciones_reservadas'
    )
    habitacion = models.ForeignKey(
        'habitaciones.Habitacion',
        on_delete=models.PROTECT,
        related_name='reservas_habitacion'
    )
    tarifa = models.ForeignKey(
        'tarifas.TarifaHabitacion',
        on_delete=models.PROTECT,
        related_name='reservas_habitacion'
    )
    precio_noche = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    noches = models.PositiveIntegerField()
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    estado = models.CharField(
        max_length=30,
        choices=ESTADO_CHOICES,
        default='activa'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Habitación reservada'
        verbose_name_plural = 'Habitaciones reservadas'
        unique_together = ('reserva', 'habitacion')
        ordering = ['id']

    def clean(self):
        if self.reserva.fecha_salida <= self.reserva.fecha_entrada:
            raise ValidationError(
                'La reserva tiene fechas inválidas.'
            )

        existe_cruce = ReservaHabitacion.objects.filter(
            habitacion=self.habitacion,
            reserva__estado__in=['pendiente', 'confirmada'],
            reserva__fecha_entrada__lt=self.reserva.fecha_salida,
            reserva__fecha_salida__gt=self.reserva.fecha_entrada,
        ).exclude(id=self.id).exists()

        if existe_cruce:
            raise ValidationError(
                'La habitación ya está reservada en ese rango de fechas.'
            )

    def __str__(self):
        return f'{self.reserva.codigo} - {self.habitacion}'


class HuespedReserva(models.Model):
    reserva = models.ForeignKey(
        Reserva,
        on_delete=models.CASCADE,
        related_name='huespedes'
    )
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=30)
    numero_documento = models.CharField(max_length=30)
    edad = models.PositiveIntegerField(null=True, blank=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    es_titular = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Huésped de reserva'
        verbose_name_plural = 'Huéspedes de reserva'
        ordering = ['id']

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'