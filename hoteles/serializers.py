from rest_framework import serializers
from .models import Hotel, DireccionHotel

class DireccionHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DireccionHotel
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    # Esto permite incluir la dirección completa anidada cuando consultes el hotel
    direccion = DireccionHotelSerializer(read_only=True, source='direccionhotel') 

    class Meta:
        model = Hotel
        fields = '__all__'