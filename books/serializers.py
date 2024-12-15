from math import floor, ceil
from statistics import mean

from drf_spectacular.utils import extend_schema_field
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

    @extend_schema_field(int)
    def get_likes_count(self, obj):
        return obj.reviews.count()


class BookDetailSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField(method_name="get_avg_rating")

    class Meta:
        model = Book
        fields = ("id", "cover_image", "authors", "description", "pages", "rating", "borrowing_duration")

    @extend_schema_field(float)
    def get_avg_rating(self, obj):
        reviews = BookReview.objects.filter(book=obj)
        if not reviews:
            return 0
        avg_of_ratings = mean([review.rating for review in reviews])

        nearest_half = round(avg_of_ratings*2) / 2
        return nearest_half


class BookReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        exclude = ("book", )
