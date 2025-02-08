from drf_spectacular.utils import extend_schema

from apps.books import serializers
from utils.exceptions import resp


get_books_schema = extend_schema(
    summary='Get Books',
    request=None,
    responses=resp(200, serializers.BookSerializer(many=True))
)

create_book_schema = extend_schema(
    summary='Create Book',
    request=serializers.BookCreateSerializer(),
    responses=resp(201)
)

get_book_schema = extend_schema(
    summary='Get Book',
    request=None,
    responses=resp(200, serializers.BookDetailSerializer())
)

update_book_schema = extend_schema(
    summary='Update Book',
    request=serializers.BookUpdateSerializer(),
    responses=resp(200)
)

delete_book_schema = extend_schema(
    summary='Delete Book',
    request=None,
    responses=resp(204)
)

get_book_reviews_schema = extend_schema(
    summary='Get Book Reviews',
    request=None,
    responses=resp(200, serializers.ReviewSerializer(many=True))
)

write_review_schema = extend_schema(
    summary='Write Review',
    request=serializers.WriteReviewSerializer(),
    responses=resp(201)
)
