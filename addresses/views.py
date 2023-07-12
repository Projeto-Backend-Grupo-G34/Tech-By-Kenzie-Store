from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import get_object_or_404
from users.permissions import IsOwnerOrAdmin, IsInstanceOrAdmin
from users.models import User
from addresses.models import Address
from addresses.serializers import AddressSerializer
from drf_spectacular.utils import extend_schema


class AddressView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin, IsAuthenticated]

    serializer_class = AddressSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(User, pk=pk)
        return Address.objects.filter(user=user)

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(User, pk=pk)
        serializer.save(user=user)

    @extend_schema(
        operation_id="address_list",
        description="List addresses",
        summary="List Addresses",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        operation_id="address_create",
        description="Create a new address",
        summary="Create Address",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsInstanceOrAdmin]

    serializer_class = AddressSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(User, pk=pk)
        return Address.objects.filter(user=user)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs.get("address_pk"))
        self.check_object_permissions(self.request, obj)
        print(obj)
        return obj
    
    def perform_update(self, serializer):
        serializer.save()

    @extend_schema(
        operation_id="address_retrieve",
        description="Retrieve an address by ID",
        summary="Retrieve Address",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        operation_id="address_put",
        description="Update an address by ID",
        summary="Update Address",
        exclude=True
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        operation_id="address_patch",
        description="Partially update an address by ID",
        summary="Update Address",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        operation_id="address_delete",
        description="Delete an address by ID",
        summary="Delete Address",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)