from rest_framework import generics
from django.shortcuts import get_object_or_404
from users.models import User
from addresses.models import Address
from addresses.serializers import AddressSerializer


class AddressView(generics.ListCreateAPIView):
    serializer_class = AddressSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(User, pk=pk)
        return Address.objects.filter(user=user)

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        user = get_object_or_404(User, pk=pk)
        serializer.save(user=user)