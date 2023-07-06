from django.urls import path
from users.views import UserListView, UserRegisterView, UserDetailView
from addresses.views import AddressView, AddressDetailView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("users/", UserListView.as_view()),
    path("users/register/", UserRegisterView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/<int:pk>/addresses/", AddressView.as_view()),
    path("users/<int:pk>/addresses/<int:address_pk>/", AddressDetailView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
]
