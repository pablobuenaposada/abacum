import pytest
from django.core.management import call_command

from transaction.models import Account, Transaction


@pytest.mark.django_db
class TestLoader:
    def test_valid(self):
        assert Account.objects.count() == 0
        assert Transaction.objects.count() == 0

        call_command("loader", "src/tests/transaction/fixtures/valid.csv")

        assert Account.objects.count() == 1
        assert Transaction.objects.count() == 1
