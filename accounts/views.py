from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import PerfilUsuario
from .serializers import (
    RegistroSerializer,
    PerfilUsuarioSerializer
)


class RegistroView(generics.CreateAPIView):
    serializer_class = RegistroSerializer
    permission_classes = [AllowAny]   # 👈 AQUÍ va


class PerfilView(generics.RetrieveAPIView):
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.perfil