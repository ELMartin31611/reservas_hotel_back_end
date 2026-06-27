from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Temporada, TarifaHabitacion
from .serializers import TemporadaSerializer, TarifaHabitacionSerializer


class TemporadaViewSet(viewsets.ModelViewSet):
    queryset = Temporada.objects.all()
    serializer_class = TemporadaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filterset_fields = ['is_active']
    search_fields = ['nombre', 'descripcion']
    ordering_fields = ['id', 'nombre', 'fecha_inicio', 'fecha_fin']
    ordering = ['fecha_inicio']


class TarifaHabitacionViewSet(viewsets.ModelViewSet):
    queryset = TarifaHabitacion.objects.select_related(
        'tipo_habitacion',
        'temporada'
    ).all()
    serializer_class = TarifaHabitacionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filterset_fields = [
        'tipo_habitacion',
        'temporada',
        'is_active',
        'moneda',
    ]
    search_fields = [
        'tipo_habitacion__nombre',
        'temporada__nombre',
    ]
    ordering_fields = [
        'id',
        'precio_noche',
        'precio_fin_semana',
        'created_at',
    ]
    ordering = ['id']