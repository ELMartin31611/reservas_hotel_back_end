from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerReservaOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True

        if hasattr(obj, 'cliente'):
            return obj.cliente.perfil.user == request.user

        if hasattr(obj, 'reserva'):
            return obj.reserva.cliente.perfil.user == request.user

        return False