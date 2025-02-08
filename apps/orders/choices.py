from django.db.models import TextChoices


class OrderStatusChoice(TextChoices):

    WAITING = 'WAITING'
    CONFIRMED = 'CONFIRMED'
    CANCELED = 'CANCELED'
    FINISHED = 'FINISHED'
