from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "image")


class BookListSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(method_name="get_likes_count")

    class Meta:
        model = Book
        fields = ("id", "title", "authors", "category", "cover_image", "comments")

    def get_likes_count(self, obj):
        return obj.reviews.count()