from rest_framework import permissions
from rest_framework.views import Request, View

from users.models import User


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.user.is_authenticated and (request.user.is_superuser or obj == request.user):
            return True
        return False
    
class IsVendorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.user.is_authenticated and (request.user.is_employee or request.user.is_superuser):
            return True
        return False