from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from django.db.models import Q

from apps.orders.choices import OrderStatusChoice
from apps.orders.models import Order


def cancel_expired_reservations():
    expired_orders = Order.objects.filter(
        Q(status=OrderStatusChoice.CONFIRMED) &
        Q(start_date__lt=now() - timedelta(days=1))
    )

    for order in expired_orders:
        book = order.book
        order.status = OrderStatusChoice.CANCELED
        order.save(update_fields=['status'])

        if book.count == 0:
            book.is_available = True
        book.count += 1
        book.save(update_fields=['count', 'is_available'])

    return True


class Command(BaseCommand):
    help = "Check orders"

    def handle(self, *args, **kwargs):
        result = cancel_expired_reservations()
        self.stdout.write(self.style.SUCCESS("Success!"))
