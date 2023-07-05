from django.urls import path
from users.views import UserView, UserDetailView
from addresses.views import AddressView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/<int:pk>/addresses/", AddressView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
]
