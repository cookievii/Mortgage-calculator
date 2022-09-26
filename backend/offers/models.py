from django.db import models


class Bank(models.Model):
    bank_name = models.CharField(max_length=255, verbose_name="Наименование банка")

    def __str__(self):
        return self.bank_name


class Offer(models.Model):
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, verbose_name="Банк", related_name="offer"
    )
    term_min = models.PositiveSmallIntegerField(verbose_name="Срок ипотеки, ОТ")
    term_max = models.PositiveSmallIntegerField(verbose_name="Срок ипотеки, ДО")
    rate_min = models.FloatField(verbose_name="Ставка, ОТ")
    rate_max = models.FloatField(verbose_name="Ставка, ДО")
    payment_min = models.PositiveIntegerField(verbose_name="Сумма кредита, ОТ")
    payment_max = models.PositiveIntegerField(verbose_name="Сумма кредита, ДО")

    def __str__(self):
        return str(self.rate_min)
