from django.urls import path


from books.views import CategoryListAPIView, BookListAPIView, BookDetailAPIView, BookReviewListAPIView, CreateBorrowAPIView

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='books'),
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('<int:id>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('<int:id>/reviews/', BookReviewListAPIView.as_view(), name='reviews'),
    path('borrows/create/', CreateBorrowAPIView.as_view(), name='create-borrow'),
]