from django.core.exceptions import ValidationError
from django.db import models

from transaction.validators import validate_amount


class Account(models.Model):
    id = models.PositiveIntegerField(primary_key=True, null=False, blank=False)

    def balance(self, year=None, month=None):
        if not year and month:
            raise ValidationError("balance for specific month needs also specific year")

        balance = 0
        qs = self.transaction_set.all()  # get all transactions by this account
        if year:
            qs = qs.filter(created__year__lte=year)
        if month:
            qs = qs.filter(created__month__lte=month)
        for transaction in qs:
            # add up all the chosen amounts
            balance += transaction.amount
        return balance


class Transaction(models.Model):
    created = models.DateTimeField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, **kwargs):
        validate_amount(self.amount)
        super().save(**kwargs)
