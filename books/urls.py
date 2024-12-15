from django.urls import path

from books.views import CategoryListAPIView, BookListAPIView, BookDetailAPIView, BookReview, BookReviewListAPIView

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='books'),
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('<int:id>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('<int:id>/reviews/', BookReviewListAPIView.as_view(), name='reviews'),
]