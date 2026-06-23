from rest_framework import serializers
from .models import TipoHabitacion, Cama, TipoHabitacionCama, Habitacion, ImagenHabitacion

class TipoHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacion
        fields = '__all__'

class CamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cama
        fields = '__all__'

class TipoHabitacionCamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoHabitacionCama
        fields = '__all__'

class ImagenHabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenHabitacion
        fields = '__all__'

class HabitacionSerializer(serializers.ModelSerializer):
    imagenes = ImagenHabitacionSerializer(many=True, read_only=True)
    tipo_detalle = TipoHabitacionSerializer(read_only=True, source='tipo')

    class Meta:
        model = Habitacion
        fields = '__all__'