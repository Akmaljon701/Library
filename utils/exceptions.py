import os
import requests
from django.db.models import IntegerChoices
from rest_framework.exceptions import APIException
from rest_framework import exceptions, serializers
from rest_framework.views import exception_handler
from rest_framework.response import Response
from dotenv import load_dotenv

load_dotenv()


class ErrorCodes(IntegerChoices):
    SOMETHING_WENT_WRONG = 400_001
    USER_NOT_FOUND = 400_002
    BOOK_NOT_FOUND = 400_003
    ORDER_NOT_FOUND = 400_004
    NO_BOOK = 400_005
    INCORRECT_RATING_VALUE = 400_006


def exception(exp_class, error_code: ErrorCodes, message) -> APIException:
    exp = exp_class({
        'error_code': error_code,
        'message': message,
    })
    return exp

def raise_error(error_code, message = "Something went wrong."):
    raise exception(
        exceptions.ValidationError,
        error_code,
        message,
    )


class ResponseSerializer(serializers.Serializer):
    error_code = serializers.CharField(max_length=7)
    message = serializers.CharField(max_length=100)


def resp(code, ser_class = ""):
    return {
        code: ser_class,
        400: ResponseSerializer()
    }


def send_me(message):
    try:
        token = os.getenv('BOT_TOKEN')
        chat_id = os.getenv('CHAT_ID')
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            'chat_id': chat_id,
            'text': message
        }
        requests.post(url=url, params=data)
    except Exception as e:
        print(f"Error while sending message to telegram: {e}")


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        return response
    if bool(os.getenv('IS_SERVER')):
        send_me(f"Library:\n{exc}")
    return Response(
        {
            "error_code": "500_500",
            "message": str(exc)
        },
        status=400
    )

