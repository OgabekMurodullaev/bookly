from django.urls import path

from books.views import CategoryListAPIView, BookListAPIView

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='books'),
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
]