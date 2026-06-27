from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Reserva, ReservaHabitacion, HuespedReserva
from .serializers import (
    ReservaSerializer,
    ReservaHabitacionSerializer,
    HuespedReservaSerializer,
)
from .permissions import IsOwnerReservaOrAdmin


class ReservaViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated, IsOwnerReservaOrAdmin]

    filterset_fields = ['estado', 'cliente']
    search_fields = ['codigo', 'cliente__nombres', 'cliente__apellidos']
    ordering_fields = ['id', 'fecha_entrada', 'fecha_salida', 'created_at', 'total']
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = Reserva.objects.select_related(
            'cliente',
            'cliente__perfil',
            'cliente__perfil__user'
        ).prefetch_related(
            'habitaciones_reservadas',
            'huespedes'
        )

        if self.request.user.is_staff:
            return queryset

        return queryset.filter(cliente__perfil__user=self.request.user)


class ReservaHabitacionViewSet(viewsets.ModelViewSet):
    serializer_class = ReservaHabitacionSerializer
    permission_classes = [IsAuthenticated, IsOwnerReservaOrAdmin]

    filterset_fields = ['reserva', 'habitacion', 'estado']
    search_fields = ['reserva__codigo', 'habitacion__numero']
    ordering_fields = ['id', 'created_at', 'subtotal']
    ordering = ['id']

    def get_queryset(self):
        queryset = ReservaHabitacion.objects.select_related(
            'reserva',
            'reserva__cliente',
            'reserva__cliente__perfil',
            'habitacion',
            'tarifa'
        )

        if self.request.user.is_staff:
            return queryset

        return queryset.filter(
            reserva__cliente__perfil__user=self.request.user
        )


class HuespedReservaViewSet(viewsets.ModelViewSet):
    serializer_class = HuespedReservaSerializer
    permission_classes = [IsAuthenticated, IsOwnerReservaOrAdmin]

    filterset_fields = ['reserva', 'tipo_documento', 'es_titular']
    search_fields = ['nombres', 'apellidos', 'numero_documento']
    ordering_fields = ['id', 'created_at']
    ordering = ['id']

    def get_queryset(self):
        queryset = HuespedReserva.objects.select_related(
            'reserva',
            'reserva__cliente',
            'reserva__cliente__perfil'
        )

        if self.request.user.is_staff:
            return queryset

        return queryset.filter(
            reserva__cliente__perfil__user=self.request.user
        )