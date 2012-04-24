from django.contrib import admin
from library.books.models import Book, Purchase, Sale

admin.site.register(Book)
admin.site.register(Purchase)
admin.site.register(Sale)