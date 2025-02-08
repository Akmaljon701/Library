from django.contrib import admin

from apps.books.models import Review, Book

admin.site.register(Book)
admin.site.register(Review)
