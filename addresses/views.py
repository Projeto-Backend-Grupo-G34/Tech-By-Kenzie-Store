from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from django.shortcuts import get_object_or_404
from users.permissions import IsOwnerOrAdmin, IsInstanceOrAdmin
from users.models import User
from addresses.models import Address
from addresses.serializers import AddressSerializer


class AddressView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    serializer_class = AddressSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(User, pk=pk)
        return Address.objects.filter(user=user)

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(User, pk=pk)
        serializer.save(user=user)

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