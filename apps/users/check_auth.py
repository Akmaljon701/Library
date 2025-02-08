from functools import wraps
from random import randint

import pytz
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from datetime import timedelta, datetime
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class IPThrottle(UserRateThrottle):
    rate = '5/min'


def generate_sms_code():
    return randint(1000, 9999)

def get_token(user):
    refresh = RefreshToken.for_user(user)
    access_expiration = datetime.fromtimestamp(refresh.access_token['exp'], pytz.utc).timestamp() * 1000
    refresh_expiration = datetime.fromtimestamp(refresh['exp'], pytz.utc).timestamp() * 1000

    return {
        "access_token": str(refresh.access_token),
        "access_expiration_date": access_expiration,
        "refresh_token": str(refresh),
        "refresh_expiration_date": refresh_expiration
    }

def update_token(refresh_token):
    refresh = RefreshToken(refresh_token)
    access_expiration = datetime.fromtimestamp(refresh.access_token['exp'], pytz.utc).timestamp() * 1000
    refresh_expiration = datetime.fromtimestamp(refresh['exp'], pytz.utc).timestamp() * 1000

    return {
        "access_token": str(refresh.access_token),
        "access_expiration_date": access_expiration,
        "refresh_token": str(refresh),
        "refresh_expiration_date": refresh_expiration
    }

def blacklist(refresh):
    token = RefreshToken(refresh)
    token.blacklist()
    return True


def permission(roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            if request.user.role in ['ADMIN'] + roles:
                return view_func(request, *args, **kwargs)
            else:
                return Response({'detail': 'You don\'t have permission to perform this action.'}, 403)
        return wrapper_func
    return decorator


