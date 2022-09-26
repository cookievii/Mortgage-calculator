from api.serializers import OfferSerializer
from django.test import Client, TestCase
from django.urls import reverse
from offers.models import Bank, Offer
from rest_framework import status


class RESTTests(TestCase):
    @classmethod
    def setUpClass(self):
        """Фикстуры для тестов."""
        super().setUpClass()
        self.guest_client = Client()
        self.bank_1 = Bank.objects.create(bank_name="Тестовый банк_1")
        self.bank_2 = Bank.objects.create(bank_name="Тестовый банк_2")
        self.offer1 = Offer.objects.create(
            bank=self.bank_1,
            term_min=3,
            term_max=15,
            rate_min=4.6,
            rate_max=15.3,
            payment_min=600_000,
            payment_max=10_000_000,
        )

        self.offer2 = Offer.objects.create(
            bank=self.bank_2,
            term_min=3,
            term_max=10,
            rate_min=4.6,
            rate_max=15.3,
            payment_min=500_000,
            payment_max=50_000_000,
        )

        self.valid_offer = {
            "bank_name": "Валидное название банка",
            "term_min": 1,
            "term_max": 10,
            "rate_min": 6.6,
            "rate_max": 15.0,
            "payment_min": 100_000,
            "payment_max": 10_000_000,
        }

        self.invalid_offer = {
            "bank_name": "",
            "term_min": 1,
            "rate_min": 1.6,
            "rate_max": 14.3,
            "payment_min": 50_000,
            "payment_max": 70_000_000,
        }

    def test_get_all_offers(self):
        """Проверяем list запрос."""
        response = self.guest_client.get(reverse("offer-list"))
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_offer(self):
        """Проверяем get запрос."""
        response = self.guest_client.get(
            reverse("offer-detail", kwargs={"pk": self.offer1.pk})
        )
        offer = Offer.objects.get(pk=self.offer1.pk)
        serializer = OfferSerializer(offer)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_offer(self):
        """Проверяем create запрос c валидными данными."""
        response = self.guest_client.post(
            reverse("offer-list"),
            data=self.valid_offer,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_offer(self):
        """Проверяем create запрос c невалидными данными."""
        response = self.guest_client.post(
            reverse("offer-list"),
            data=self.invalid_offer,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_offer(self):
        """Проверяем put запрос c валидными данными."""
        response = self.guest_client.put(
            reverse("offer-detail", kwargs={"pk": self.offer1.pk}),
            data=self.valid_offer,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_offer(self):
        """Проверяем put запрос c невалидными данными."""
        response = self.guest_client.put(
            reverse("offer-detail", kwargs={"pk": self.offer1.pk}),
            data=self.invalid_offer,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_delete_offer(self):
        """Проверяем delete запрос."""
        response = self.guest_client.delete(
            reverse("offer-detail", kwargs={"pk": self.offer1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_offer(self):
        """Проверяем delete запрос."""
        response = self.guest_client.delete(
            reverse("offer-detail", kwargs={"pk": 9999})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
