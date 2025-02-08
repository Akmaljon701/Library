from rest_framework.decorators import api_view
from apps.books import services as svc
from apps.users.check_auth import permission
from apps.books import schemas as schm


@schm.get_books_schema
@api_view(['GET'])
@permission(['OPERATOR', 'USER'])
def get_books(request):
    return svc.BookService(request).get_books()


@schm.create_book_schema
@api_view(['POST'])
@permission(['OPERATOR'])
def create_book(request):
    return svc.BookService(request).create_book()


@schm.get_book_schema
@api_view(['GET'])
@permission(['OPERATOR', 'USER'])
def get_book(request, pk):
    return svc.BookService(request).get_book(pk)


@schm.update_book_schema
@api_view(['PUT'])
@permission(['OPERATOR'])
def update_book(request, pk):
    return svc.BookService(request).update_book(pk)


@schm.delete_book_schema
@api_view(['DELETE'])
@permission(['OPERATOR'])
def delete_book(request, pk):
    return svc.BookService(request).delete_book(pk)


@schm.get_book_reviews_schema
@api_view(['GET'])
@permission(['OPERATOR', 'USER'])
def get_book_reviews(request, pk):
    return svc.ReviewService(request).get_book_reviews(pk)


@schm.write_review_schema
@api_view(['POST'])
@permission(['USER'])
def write_review(request):
    return svc.ReviewService(request).write_review()

