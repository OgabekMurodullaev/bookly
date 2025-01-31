from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from yaml import serialize

from books.filters import BookFilter
from books.models import Category, Book, BookReview, Borrow
from books.serializers import CategorySerializer, BookListSerializer, BookDetailSerializer, BookReviewListSerializer, \
    CreateBorrowSerializer


class CategoryListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class BookDetailAPIView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = BookDetailSerializer

    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)
            serializer = BookDetailSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Book.DoesNotExist:
            data = {
                "message": "Book not found"
            }

            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(f"{e}")


class BookReviewListAPIView(APIView):
    permission_classes = [AllowAny, ]
    serializer_class = BookReviewListSerializer

    def get(self, request, id):
        book = Book.objects.get(id=id)
        reviews = BookReview.objects.filter(book=book)
        if not reviews:
            return Response(data={"detail": "No reviews found"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BookReviewListSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateBorrowAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CreateBorrowSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "You successfully borrowed this book"
            }

            return Response(data=data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReturnBookAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = CreateBorrowSerializer

    def put(self, request, borrow_id):
        try:
            borrow = Borrow.objects.get(id=borrow_id, user=request.user)
            if borrow.status == "returned":
                return Response(data={"detail": "This book has already been returned"}, status=status.HTTP_400_BAD_REQUEST)

            borrow.status = "returned"
            borrow.save()
            data = {
                "detail": "You have successfully returned this book"
            }
            return Response(data=data, status=status.HTTP_200_OK)

        except Exception as e:
            return f"{e}"
