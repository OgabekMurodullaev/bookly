from rest_framework import generics
from rest_framework.permissions import AllowAny

from books.models import Category
from books.serializers import CategorySerializer


class CategoryListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

