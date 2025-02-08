from rest_framework import serializers

from utils.exceptions import raise_error, ErrorCodes
from .models import Book, Review


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'count',
            'daily_price',
            'is_available',
            'created_at',
        ]


class BookDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'description',
            'count',
            'daily_price',
            'is_available',
            'created_at',
        ]


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
            'count',
            'daily_price',
        ]


class BookUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
            'count',
            'daily_price',
        ]


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'rating',
            'comment',
            'created_at',
        ]


class WriteReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'book',
            'rating',
            'comment'
        ]

    def validate_rating(self, value):
        if value < 0 or value > 5:
            raise raise_error(
                ErrorCodes.INCORRECT_RATING_VALUE,
                "Incorrect rating value."
            )
        return value