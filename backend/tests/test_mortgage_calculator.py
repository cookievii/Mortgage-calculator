from django.test import Client, TestCase
from offers.models import Bank, Offer


class MortgageCalculatorTest(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.guest_client = Client()
        self.bank = Bank.objects.create(bank_name="Тестовый банк_1")
        self.offer1 = Offer.objects.create(
            bank=self.bank,
            term_min=3,
            term_max=15,
            rate_min=4.6,
            rate_max=15.3,
            payment_min=600_000,
            payment_max=10_000_000,
        )

    def test_calculator_with_request(self):
        """Проверяем калькулятор через запрос."""
        url = f"/api/offer/?price={10_000_000}&deposit={1_000_000}&term={15}"
        result = 69_310
        response = self.guest_client.get(url)
        self.assertEqual(response.data[0].get("payment"), result)
