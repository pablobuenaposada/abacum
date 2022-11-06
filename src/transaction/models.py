from django.db import models

from transaction.validators import validate_amount


class Account(models.Model):
    id = models.PositiveIntegerField(primary_key=True, null=False, blank=False)


class Transaction(models.Model):
    created = models.DateTimeField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, **kwargs):
        validate_amount(self.amount)
        super().save(**kwargs)
