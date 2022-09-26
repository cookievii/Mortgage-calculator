from django.db.models import Q
from django_filters import CharFilter, NumberFilter
from django_filters.rest_framework import FilterSet


class OfferFilter(FilterSet):
    rate_min = NumberFilter(field_name="rate_min", lookup_expr="gte")
    rate_max = NumberFilter(field_name="rate_max", lookup_expr="lte")
    term = CharFilter(method="filter_term", label="term")
    payment_min = NumberFilter(field_name="payment", lookup_expr="gte")
    payment_max = NumberFilter(field_name="payment", lookup_expr="lte")
    order = CharFilter(method="filter_order", label="order")

    @classmethod
    def filter_term(cls, queryset, name, value):
        return queryset.filter(Q(term_min__lte=value) | Q(term_max__gte=value))

    @classmethod
    def filter_order(cls, queryset, name, value):
        return queryset.order_by("rate_min")
