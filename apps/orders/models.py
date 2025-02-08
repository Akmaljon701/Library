from django.db import models
from django.utils.timezone import now

from apps.orders.choices import OrderStatusChoice
from apps.users.models import CustomUser
from apps.books.models import Book


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orders')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    returned_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=OrderStatusChoice.choices,
        default=OrderStatusChoice.WAITING
    )

    @property
    def fine_amount(self):
        overdue_days = (self.returned_at or now()) - self.end_date
        overdue_days = overdue_days.days

        if overdue_days > 0:
            return round(overdue_days * (self.book.daily_price * 0.01), 2)

        return 0

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
