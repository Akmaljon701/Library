from rest_framework.response import Response

from utils.exceptions import raise_error, ErrorCodes
from utils.pagination import BaseService, BaseServicePagination
from apps.books import models as books_models
from apps.books import serializers


class BookService(BaseServicePagination):

    def get_books(self):
        books = books_models.Book.objects.all().order_by('-created_at')
        results = self.paginate(books)
        serializer = serializers.BookSerializer(
            results,
            many=True
        )
        return self.paginated_response(serializer.data)

    def create_book(self):
        serializer = serializers.BookCreateSerializer(
            data=self.request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)

    def get_book(self, pk):
        serializer = serializers.BookDetailSerializer(
            self._get_book(pk)
        )
        return Response(serializer.data)

    def update_book(self, pk):
        serializer = serializers.BookUpdateSerializer(
            self._get_book(pk),
            data=self.request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=200)

    def delete_book(self, pk):
        book = self._get_book(pk)
        book.delete()
        return Response(status=204)

    def _get_book(self, pk):
        try:
            book = books_models.Book.objects.get(id=pk)
        except books_models.Book.DoesNotExist:
            raise raise_error(
                ErrorCodes.BOOK_NOT_FOUND,
                "Book not found."
            )
        return book


class ReviewService(BaseServicePagination):

    def get_book_reviews(self, pk):
        book = self._get_book(pk)
        results = self.paginate(book.reviews.all().order_by("-created_at"))
        serializer = serializers.ReviewSerializer(
            results,
            many=True
        )
        return self.paginated_response(serializer.data)

    def write_review(self):
        serializer = serializers.WriteReviewSerializer(
            data=self.request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(status=201)

    def _get_book(self, pk):
        try:
            book = books_models.Book.objects.prefetch_related('reviews').get(id=pk)
        except books_models.Book.DoesNotExist:
            raise raise_error(
                ErrorCodes.BOOK_NOT_FOUND,
                "Book not found."
            )
        return book
