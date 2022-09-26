from django.db.models import F, IntegerField, Sum
from offers.models import Offer


class OfferRepository:
    def __init__(self):
        self.model = Offer.objects.select_related("bank")

    def get_all(self) -> Offer:
        """Метод для получения всех 'Offer'."""
        return self.model.all()


class PaymentRepository:
    def __init__(self):
        self.queryset = OfferRepository().get_all()
        self.__MO = 1
        self.__MO_IN_YEAR = 12
        self.__FULL_PERCENT = 100
        self.price = None
        self.deposit = None
        self.term = None

    def validated_data(self, price=None, deposit=None, term=None) -> bool:
        """Метод валидации входных данных."""
        try:
            self.price = int(price)
            self.deposit = int(deposit)
            self.term = int(term)
            return True
        except TypeError:
            return False

    def make_calc_payment(self) -> Offer:
        """Расчет аннуитетного платежа.
        Формула взята с сайта:
        https://www.raiffeisen.ru/wiki/kak-rasschitat-annuitetnyj-platezh/"""
        DEBT = self.price - self.deposit
        PERC_PER_MO = F("rate_min") / (self.__FULL_PERCENT * self.__MO_IN_YEAR)
        LOAN_TERM = -self.__MO_IN_YEAR * self.term
        PERC_BY_DURATIONS = self.__MO - ((PERC_PER_MO + self.__MO) ** LOAN_TERM)
        return (
            self.queryset.annotate(
                payment=Sum(
                    (PERC_PER_MO / PERC_BY_DURATIONS) * DEBT,
                    output_field=IntegerField(),
                )
            )
        )

    def get_queryset_with_payment(self, price, deposit, term) -> Offer:
        """Запуск калькуляции 'payment'."""
        validated_data = self.validated_data(price, deposit, term)
        if validated_data:
            return self.make_calc_payment()
        return self.queryset
