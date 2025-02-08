from django.db.models import TextChoices


class UserRoleChoice(TextChoices):

    ADMIN = 'ADMIN'
    USER = 'USER'
    OPERATOR = 'OPERATOR'
