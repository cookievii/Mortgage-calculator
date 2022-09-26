from api.filters import OfferFilter
from api.repositories import PaymentRepository as PR
from api.serializers import OfferSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OfferFilter

    def get_queryset(self):
        price = self.request.query_params.get("price")
        deposit = self.request.query_params.get("deposit")
        term = self.request.query_params.get("term")

        return PR().get_queryset_with_payment(price, deposit, term)
