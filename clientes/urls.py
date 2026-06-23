from rest_framework.routers import DefaultRouter
from .views import (
    ClienteViewSet,
    DireccionClienteViewSet,
    DocumentoClienteViewSet
)

router = DefaultRouter()

router.register('clientes', ClienteViewSet)
router.register('direcciones', DireccionClienteViewSet)
router.register('documentos', DocumentoClienteViewSet)

urlpatterns = router.urls