from django.contrib import admin
from .models import (
    TipoHabitacion,
    Habitacion,
    Cama,
    TipoHabitacionCama,
    ImagenHabitacion
)

admin.site.register(TipoHabitacion)
admin.site.register(Habitacion)
admin.site.register(Cama)
admin.site.register(TipoHabitacionCama)
admin.site.register(ImagenHabitacion)