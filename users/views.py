from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from users.permissions import IsOwnerOrAdmin
from users.models import User
from users.serializers import UserSerializer
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class UserListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        operation_id="user_list",
        description="List users",
        summary="List Users",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        operation_id="user_create",
        description="Register a new user",
        summary="Register User",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        operation_id="user_retrieve",
        description="Retrieve a user by ID",
        summary="Retrieve User",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_put",
        description="Update a user by ID",
        summary="Update User",
        exclude=True,
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_patch",
        description="Partially update a user by ID",
        summary="Update User",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_delete",
        description="Delete a user by ID",
        summary="Delete User",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CustomTokenObtainPairView(TokenObtainPairView):
    @extend_schema(
        operation_id="token_obtain_pair",
        description="Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.",
        summary="Obtain Access and Refresh Token Pair",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    @extend_schema(
        operation_id="token_refresh",
        description="Refresh an access token using a refresh token.",
        summary="Refresh Access Token",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
