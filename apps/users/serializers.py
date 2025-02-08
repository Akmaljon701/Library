from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class TokenResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    access_expiration_date = serializers.IntegerField()
    refresh_token = serializers.CharField()
    refresh_expiration_date = serializers.IntegerField()


class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
