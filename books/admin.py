from django.contrib import admin

from .models import Author, Category, Book, BookReview, BookAuthors

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(BookReview)
admin.site.register(BookAuthors)