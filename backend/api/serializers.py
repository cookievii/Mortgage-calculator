from offers.models import Bank, Offer
from rest_framework import serializers


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ("bank_name",)


class OfferSerializer(serializers.ModelSerializer):
    payment = serializers.SerializerMethodField()
    bank_name = serializers.PrimaryKeyRelatedField(
        read_only=True, many=False, source="bank.bank_name"
    )

    class Meta:
        model = Offer
        fields = (
            "id",
            "bank_name",
            "payment",
            "term_min",
            "term_max",
            "rate_min",
            "rate_max",
            "payment_min",
            "payment_max",
        )

    @staticmethod
    def get_payment(obj):
        return obj.__dict__.get("payment")

    def create(self, validated_data):
        bank_name = self.initial_data.get("bank_name")
        bank, was_created_new_bank = Bank.objects.get_or_create(bank_name=bank_name)
        if was_created_new_bank:
            bank.save()

        offer = Offer.objects.create(bank=bank, **validated_data)
        return offer

    def update(self, instance, validated_data):
        instance.bank.bank_name = self.initial_data.get(
            "bank_name", instance.bank.bank_name
        )

        instance.term_min = validated_data.get("term_min", instance.term_min)
        instance.term_max = validated_data.get("term_max", instance.term_max)
        instance.rate_min = validated_data.get("rate_min", instance.rate_min)
        instance.rate_max = validated_data.get("rate_max", instance.rate_max)
        instance.payment_min = validated_data.get("payment_min", instance.payment_min)
        instance.payment_max = validated_data.get("payment_max", instance.payment_max)
        instance.save()
        return instance
