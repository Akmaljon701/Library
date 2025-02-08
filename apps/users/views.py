from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from rest_framework.request import Request

from utils.exceptions import resp
from apps.users import serializers
from apps.users import services as svc


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        summary='Login',
        request=serializers.LoginSerializer(),
        responses=resp(200, serializers.TokenResponseSerializer())
    )
    def post(self, request: Request):
        return svc.UserAuthService(request).login()


class RefreshTokenAPIView(APIView):

    @extend_schema(
        summary='Refresh',
        request=serializers.RefreshTokenSerializer(),
        responses=resp(200, serializers.TokenResponseSerializer())
    )
    def post(self, request: Request):
        return svc.UserAuthService(request).refresh()



class LogoutAPIView(APIView):

    @extend_schema(
        summary='Logout',
        request=serializers.RefreshTokenSerializer(),
        responses=resp(204)
    )
    def post(self, request: Request):
        return svc.UserAuthService(request).logout()