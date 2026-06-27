from rest_framework import serializers
from .models import Temporada, TarifaHabitacion


class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = [
            'id',
            'nombre',
            'fecha_inicio',
            'fecha_fin',
            'porcentaje_incremento',
            'descripcion',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, data):
        fecha_inicio = data.get('fecha_inicio')
        fecha_fin = data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_fin <= fecha_inicio:
            raise serializers.ValidationError(
                'La fecha fin debe ser mayor que la fecha de inicio.'
            )

        return data


class TarifaHabitacionSerializer(serializers.ModelSerializer):
    tipo_habitacion_nombre = serializers.CharField(
        source='tipo_habitacion.nombre',
        read_only=True
    )
    temporada_nombre = serializers.CharField(
        source='temporada.nombre',
        read_only=True
    )

    class Meta:
        model = TarifaHabitacion
        fields = [
            'id',
            'tipo_habitacion',
            'tipo_habitacion_nombre',
            'temporada',
            'temporada_nombre',
            'precio_noche',
            'precio_fin_semana',
            'precio_persona_extra',
            'moneda',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']