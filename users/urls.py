from django.urls import path
from users.views import UserListView, UserRegisterView, UserDetailView, CustomTokenObtainPairView, CustomTokenRefreshView
from addresses.views import AddressView, AddressDetailView


urlpatterns = [
    path("users/", UserListView.as_view()),
    path("users/register/", UserRegisterView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
    path("users/<int:pk>/addresses/", AddressView.as_view()),
    path("users/<int:pk>/addresses/<int:address_pk>/", AddressDetailView.as_view()),
    path("users/login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
]
