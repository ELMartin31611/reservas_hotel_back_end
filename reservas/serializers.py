from rest_framework import serializers
from .models import Reserva, ReservaHabitacion, HuespedReserva


class ReservaHabitacionSerializer(serializers.ModelSerializer):
    habitacion_numero = serializers.CharField(
        source='habitacion.numero',
        read_only=True
    )
    tipo_habitacion = serializers.CharField(
        source='habitacion.tipo_habitacion.nombre',
        read_only=True
    )

    class Meta:
        model = ReservaHabitacion
        fields = [
            'id',
            'reserva',
            'habitacion',
            'habitacion_numero',
            'tipo_habitacion',
            'tarifa',
            'precio_noche',
            'noches',
            'subtotal',
            'estado',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, data):
        reserva = data.get('reserva')
        habitacion = data.get('habitacion')

        if reserva and habitacion:
            existe_cruce = ReservaHabitacion.objects.filter(
                habitacion=habitacion,
                reserva__estado__in=['pendiente', 'confirmada'],
                reserva__fecha_entrada__lt=reserva.fecha_salida,
                reserva__fecha_salida__gt=reserva.fecha_entrada,
            )

            if self.instance:
                existe_cruce = existe_cruce.exclude(id=self.instance.id)

            if existe_cruce.exists():
                raise serializers.ValidationError(
                    'La habitación ya está reservada en ese rango de fechas.'
                )

        return data


class HuespedReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HuespedReserva
        fields = [
            'id',
            'reserva',
            'nombres',
            'apellidos',
            'tipo_documento',
            'numero_documento',
            'edad',
            'telefono',
            'es_titular',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class ReservaSerializer(serializers.ModelSerializer):
    habitaciones_reservadas = ReservaHabitacionSerializer(
        many=True,
        read_only=True
    )
    huespedes = HuespedReservaSerializer(
        many=True,
        read_only=True
    )
    cliente_nombre = serializers.CharField(
        source='cliente.nombres',
        read_only=True
    )

    class Meta:
        model = Reserva
        fields = [
            'id',
            'codigo',
            'cliente',
            'cliente_nombre',
            'fecha_entrada',
            'fecha_salida',
            'numero_noches',
            'cantidad_adultos',
            'cantidad_ninos',
            'estado',
            'subtotal',
            'impuestos',
            'descuento',
            'total',
            'observaciones',
            'habitaciones_reservadas',
            'huespedes',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, data):
        fecha_entrada = data.get(
            'fecha_entrada',
            getattr(self.instance, 'fecha_entrada', None)
        )
        fecha_salida = data.get(
            'fecha_salida',
            getattr(self.instance, 'fecha_salida', None)
        )

        if fecha_entrada and fecha_salida and fecha_salida <= fecha_entrada:
            raise serializers.ValidationError(
                'La fecha de salida debe ser mayor que la fecha de entrada.'
            )

        return data

    def create(self, validated_data):
        fecha_entrada = validated_data.get('fecha_entrada')
        fecha_salida = validated_data.get('fecha_salida')

        if fecha_entrada and fecha_salida:
            validated_data['numero_noches'] = (
                fecha_salida - fecha_entrada
            ).days

        return super().create(validated_data)