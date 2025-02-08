from django.db import transaction
from django.contrib.auth.base_user import BaseUserManager

from utils.cryptography import encrypt_password
from utils.exceptions import raise_error, ErrorCodes
from apps.users import models as users_models


class CustomUserManager(BaseUserManager):
    @transaction.atomic
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')

        if not password:
            raise ValueError('Password must be set')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        users_models.CustomUserPasswordLog.objects.create(
            user=user,
            raw_password=encrypt_password(password)
        )
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if not all([
            extra_fields['is_staff'],
            extra_fields['is_active'],
            extra_fields['is_superuser']
        ]):
            raise ValueError('Superuser must have is_staff=True, is_active=True, and is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

    def get_user(self, pk):
        try:
            return self.get(pk=pk)
        except self.model.DoesNotExist:
            raise raise_error(
                ErrorCodes.USER_NOT_FOUND,
                "User not found."
            )