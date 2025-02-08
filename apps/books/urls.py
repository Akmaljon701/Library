from django.urls import path
from apps.books import views

urlpatterns = [
    path('', views.get_books, name='get_books'),
    path('create/', views.create_book, name='create_book'),
    path('<int:pk>/', views.get_book, name='get_book'),
    path('<int:pk>/update/', views.update_book, name='update_book'),
    path('<int:pk>/delete/', views.delete_book, name='delete_book'),

    path('<int:pk>/reviews/', views.get_book_reviews, name='get_book_reviews'),
    path('reviews/', views.write_review, name='write_review'),
]
