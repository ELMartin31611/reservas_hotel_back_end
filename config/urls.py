"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importamos las vistas de tus tres aplicaciones
from hoteles.views import HotelViewSet, DireccionHotelViewSet
from habitaciones.views import (
    HabitacionViewSet, 
    TipoHabitacionViewSet, 
    CamaViewSet, 
    TipoHabitacionCamaViewSet, 
    ImagenHabitacionViewSet
)
from servicios.views import ServicioViewSet

# Creamos el router para registrar los ViewSets
router = DefaultRouter()

# Endpoints del módulo Hoteles
router.register(r'hoteles', HotelViewSet, basename='hotel')
router.register(r'direcciones-hoteles', DireccionHotelViewSet, basename='direccion-hotel')

# Endpoints del módulo Habitaciones
router.register(r'habitaciones', HabitacionViewSet, basename='habitacion')
router.register(r'tipos-habitaciones', TipoHabitacionViewSet, basename='tipo-habitacion')
router.register(r'camas', CamaViewSet, basename='cama')
router.register(r'configuracion-camas', TipoHabitacionCamaViewSet, basename='config-cama')
router.register(r'imagenes-habitaciones', ImagenHabitacionViewSet, basename='imagen-habitacion')

# Endpoints del módulo Servicios
router.register(r'servicios', ServicioViewSet, basename='servicio')

# Rutas globales del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Aquí se incluyen automáticamente todos tus CRUDs
]