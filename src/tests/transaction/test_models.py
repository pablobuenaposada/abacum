from datetime import datetime

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
        """
        Trying to create an Account with the same id should raise an error
        """
        data = {"id": 1}
        Account.objects.create(**data)

        with pytest.raises(IntegrityError):
            Account.objects.create(**data)

    @pytest.mark.parametrize(
        "transactions, year, month, expected_balance",
        [
            ([], None, None, 0),
            (
                [{"amount": 1, "created": datetime(2022, 1, 1)}],
                None,
                None,
                1,
            ),  # entire life of the account
            (
                [{"amount": 1, "created": datetime(2022, 1, 1)}],
                2022,
                None,
                1,
            ),  # specific year
            (
                [{"amount": 1, "created": datetime(2022, 1, 1)}],
                2022,
                1,
                1,
            ),  # specific year and month
            (
                [{"amount": 1, "created": datetime(2022, 1, 1)}],
                2022,
                12,
                1,
            ),  # transaction first month but we ask for balance by the end of the year
            (
                [{"amount": 1, "created": datetime(2022, 1, 1)}],
                2021,
                1,
                0,
            ),  # year without transactions
            (
                [{"amount": 1, "created": datetime(2022, 2, 1)}],
                2022,
                1,
                0,
            ),  # month without transactions
            (
                [
                    {"amount": 1, "created": datetime(2022, 1, 1)},
                    {"amount": 2, "created": datetime(2022, 2, 1)},
                ],
                2022,
                2,
                3,
            ),
            (
                [
                    {"amount": 1, "created": datetime(2022, 1, 1)},
                    {"amount": 2, "created": datetime(2022, 2, 1)},
                ],
                2022,
                1,
                1,
            ),
        ],
    )
    def test_balance(self, transactions, year, month, expected_balance):
        account = baker.make(Account, id=1)
        for transaction in transactions:
            baker.make(
                Transaction,
                account=account,
                amount=transaction["amount"],
                created=transaction["created"],
            )

        assert account.balance(year, month) == expected_balance

    def test_balance_error(self):
        """
        If balance for specific month is asked year should be also defined
        """
        account = baker.make(Account)
        with pytest.raises(ValidationError) as error:
            account.balance(None, 1)

        assert (
            str(error.value)
            == "['balance for specific month needs also specific year']"
        )


@pytest.mark.django_db
class TestTransaction:
    def test_valid(self):
        account = baker.make(Account)
        data = {"account": account, "amount": 1, "created": datetime(2022, 1, 1)}
        transaction = Transaction.objects.create(**data)
        expected = {
            "id": transaction.id,
            "account": account,
            "amount": data["amount"],
            "created": transaction.created,
        }

        for field in {field.name for field in Transaction._meta.get_fields()}:
            assert getattr(transaction, field) == expected[field]

    def test_mandatory_fields(self):
        with pytest.raises(IntegrityError) as error:
            Transaction.objects.create()

        assert (
            str(error.value)
            == "NOT NULL constraint failed: transaction_transaction.amount"
        )

    def test_amount(self):
        """transaction with amount 0 is not allowed"""
        with pytest.raises(ValidationError) as error:
            Transaction.objects.create(account=baker.make(Account), amount=0)

        assert str(error.value) == "['Amount 0 is not allowed']"
