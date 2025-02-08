import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apps.users.choices import UserRoleChoice
from apps.users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer."
    )
    role = models.CharField(
        max_length=20,
        choices=UserRoleChoice.choices,
        default=UserRoleChoice.USER
    )
    device_tokens = models.JSONField(blank=True, null=True, default=list)
    is_active = models.BooleanField(
        default=False,
        help_text="Designates whether this user should be treated as active."
    )
    is_staff = models.BooleanField(
        default=False,
        help_text="Designates whether the user can log into this admin site."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class CustomUserPasswordLog(models.Model):
    user = models.ForeignKey(
        CustomUser,
        related_name="password_logs",
        on_delete=models.CASCADE
    )
    raw_password = models.CharField(
        max_length=128,
        help_text="Raw password value"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Password'
        verbose_name_plural = 'Passwords'