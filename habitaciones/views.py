from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import TipoHabitacion, Cama, TipoHabitacionCama, Habitacion, ImagenHabitacion
from .serializers import *

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer
    
    # Activamos los backends de filtrado y búsqueda de DRF
    filter_backends = [DjangoFilterBackend, SearchFilter]
    
    # Filtros exactos solicitados: tipo, estado
    filterset_fields = ['tipo', 'estado']
    
    # Búsqueda por texto (ej: buscar número de habitación o nombre del tipo)
    search_fields = ['numero', 'tipo__nombre']

# ViewSets simples para los demás modelos del módulo
class TipoHabitacionViewSet(viewsets.ModelViewSet):
    queryset = TipoHabitacion.objects.all()
    serializer_class = TipoHabitacionSerializer

class CamaViewSet(viewsets.ModelViewSet):
    queryset = Cama.objects.all()
    serializer_class = CamaSerializer

class TipoHabitacionCamaViewSet(viewsets.ModelViewSet):
    queryset = TipoHabitacionCama.objects.all()
    serializer_class = TipoHabitacionCamaSerializer

class ImagenHabitacionViewSet(viewsets.ModelViewSet):
    queryset = ImagenHabitacion.objects.all()
    serializer_class = ImagenHabitacionSerializer