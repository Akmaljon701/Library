from rest_framework import serializers

from apps.orders.choices import OrderStatusChoice
from apps.orders.models import Order
from utils.exceptions import raise_error, ErrorCodes


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'user',
            'book',
            'start_date',
            'end_date',
        ]

    def validate(self, attrs):
        book = attrs.get('book')
        if book.count <= 0:
            raise raise_error(
                ErrorCodes.NO_BOOK,
                "There is no book left."
            )
        return attrs

    def create(self, validated_data):
        book = validated_data['book']
        book.count -= 1

        if book.count == 0:
            book.is_available = False

        book.save(update_fields=['count', 'is_available'])

        return super().create(validated_data)

class OrderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = [
            'user',
            'book',
            'start_date',
            'end_date',
            'returned_at',
            'status',
        ]

    def update(self, instance, validated_data):
        old_status = instance.status
        new_status = validated_data.get("status", instance.status)
        book = instance.book

        if new_status in [OrderStatusChoice.FINISHED, OrderStatusChoice.CANCELED] and old_status in [
            OrderStatusChoice.WAITING, OrderStatusChoice.CONFIRMED]:
            if book.count == 0:
                book.is_available = True
            book.count += 1
            book.save(update_fields=['count', 'is_available'])

        return super().update(instance, validated_data)


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    book = serializers.CharField(source='book.title')

    class Meta:
        model = Order
        fields = [
            'user',
            'book',
            'start_date',
            'end_date',
            'returned_at',
            'fine_amount',
            'status'
        ]
