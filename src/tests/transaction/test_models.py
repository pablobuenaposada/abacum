import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from model_bakery import baker

from transaction.models import Account, Transaction


@pytest.mark.django_db
class TestAccount:
    def test_valid(self):
        data = {"id": 1}
        expected = data
        account = Account.objects.create(**data)

        for field in {field.name for field in Account._meta.get_fields()} - {
            "transaction"
        }:
            assert getattr(account, field) == expected[field]

    def test_mandatory_fields(self):
        with pytest.raises(IntegrityError) as error:
            Account.objects.create()

        assert str(error.value) == "NOT NULL constraint failed: transaction_account.id"

    def test_unique(self):
        data = {"id": 1}
        Account.objects.create(**data)

        with pytest.raises(IntegrityError):
            Account.objects.create(**data)


@pytest.mark.django_db
class TestTransaction:
    def test_valid(self):
        account = baker.make(Account)
        data = {"account": account, "amount": 1}
        transaction = Transaction.objects.create(**data)
        expected = {
            "id": transaction.id,
            "account": account,
            "amount": data["amount"],
            "created": transaction.created,
            "modified": transaction.modified,
        }

        for field in {field.name for field in Transaction._meta.get_fields()}:
            assert getattr(transaction, field) == expected[field]

    def test_mandatory_fields(self):
        with pytest.raises(IntegrityError) as error:
            Transaction.objects.create()

        assert (
            str(error.value)
            == "NOT NULL constraint failed: transaction_transaction.account_id"
        )

    def test_amount(self):
        """transaction with amount 0 is not allowed"""
        with pytest.raises(ValidationError) as error:
            Transaction.objects.create(account=baker.make(Account), amount=0)

        assert str(error.value) == "['Amount 0 is not allowed']"
