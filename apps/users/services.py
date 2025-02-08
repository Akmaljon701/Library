from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.check_auth import get_token, update_token
from utils.pagination import BaseService
from apps.users import serializers


class UserAuthService(BaseService):

    def login(self):
        serializer = serializers.LoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        serializer = serializers.TokenResponseSerializer(
            get_token(user)
        )
        return Response(serializer.data)

    def refresh(self):
        serializer = serializers.RefreshTokenSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data['refresh_token']
        serializer = serializers.TokenResponseSerializer(
            update_token(refresh_token)
        )
        return Response(serializer.data)

    def logout(self):
        serializer = serializers.RefreshTokenSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data['refresh_token']

        refresh = RefreshToken(refresh_token)
        refresh.blacklist()
        return Response(status=204)
