from rest_framework import permissions
from rest_framework.views import Request, View

from addresses.models import Address
from users.models import User


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.user.is_authenticated and (
            request.user.is_superuser or obj == request.user
        ):
            return True
        return False


class IsInstanceOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Address):
        if request.user.is_authenticated and (
            request.user.is_superuser or obj.user == request.user
        ):
            return True
        return False


class IsVendorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return True
            elif obj.products.filter(vendor=request.user.id).exists():
                return True
        return False


class IsVendorOrAdminForGet(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and (user.is_employee or user.is_superuser)


class IsVendorOrAdminForPost(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if (
            request.user.is_authenticated
            and request.method == "POST"
            and (request.user.is_employee or request.user.is_superuser)
            or request.method == "GET"
        ):
            return True
        return False
