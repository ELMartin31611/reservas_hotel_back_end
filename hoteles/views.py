from rest_framework import viewsets
from .models import Hotel, DireccionHotel
from .serializers import HotelSerializer, DireccionHotelSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class DireccionHotelViewSet(viewsets.ModelViewSet):
    queryset = DireccionHotel.objects.all()
    serializer_class = DireccionHotelSerializer