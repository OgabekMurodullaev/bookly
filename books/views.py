from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from books.filters import BookFilter
from books.models import Category, Book
from books.serializers import CategorySerializer, BookListSerializer


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
