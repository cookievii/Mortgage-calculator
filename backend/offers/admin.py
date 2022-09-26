from django.contrib import admin
from offers.models import Bank, Offer


@admin.register(Bank)
class Bank(admin.ModelAdmin):
    list_display = ("bank_name",)


@admin.register(Offer)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "bank",
        "term_min",
        "term_max",
        "rate_min",
        "rate_max",
        "payment_min",
        "payment_max",
    )
