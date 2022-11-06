from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from unittest.mock import ANY

import pytest

from transaction.loader import Loader
from transaction.models import Account, Transaction


@pytest.mark.django_db(transaction=True)
class TestLoader:
    def test_valid(self):
        assert Account.objects.count() == 0
        assert Transaction.objects.count() == 0

        Loader(Path("src/tests/transaction/fixtures/valid.csv"))

        assert Account.objects.count() == 1
        assert Transaction.objects.count() == 1
        expected_account = {"id": 68100000}
        for field in {field.name for field in Account._meta.get_fields()} - {
            "transaction"
        }:
            assert getattr(Account.objects.first(), field) == expected_account[field]
        expected_transaction = {
            "id": ANY,
            "created": datetime(2020, 8, 15, tzinfo=timezone.utc),
            "account": Account.objects.first(),
            "amount": Decimal("-60512.99"),
        }
        for field in {field.name for field in Transaction._meta.get_fields()}:
            assert (
                getattr(Transaction.objects.first(), field)
                == expected_transaction[field]
            )

    def test_duplicate_account(self):
        """
        Accounts cannot be duplicated, the csv may contain references to the same account multiple times
        """
        assert Account.objects.count() == 0
        assert Transaction.objects.count() == 0

        Loader(Path("src/tests/transaction/fixtures/duplicate_account.csv"))

        assert Account.objects.count() == 1
        assert Transaction.objects.count() == 2

    def test_invalid_csv(self):
        """
        Loading a csv with one account and one transaction completely fine but a second invalid transaction should end
        in no accounts or transactions loaded
        """
        assert Account.objects.count() == 0
        assert Transaction.objects.count() == 0

        with pytest.raises(Exception):
            Loader(Path("src/tests/transaction/fixtures/invalid.csv"))

        assert Account.objects.count() == 0
        assert Transaction.objects.count() == 0

    def test_csv_not_found(self):
        with pytest.raises(FileNotFoundError):
            Loader(Path("src/tests/transaction/fixtures/fake.csv"))
