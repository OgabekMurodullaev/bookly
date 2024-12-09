from django_filters import rest_framework as filters


class BookFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="category__name", lookup_expr="icontains")
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
