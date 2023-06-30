from django.urls import path
from .views import AddressView

urlpatterns = [
    path("addresses/", AddressView.as_view()),
]
