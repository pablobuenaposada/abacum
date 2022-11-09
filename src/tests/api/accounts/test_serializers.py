import pytest
from model_bakery import baker

from api.accounts.serializers import (AccountInputSerializer,
                                      AccountMonthlyOutputSerializer,
                                      AccountOutputSerializer)
from transaction.models import Transaction


@pytest.mark.django_db
class TestAccountOutputSerializer:
    def test_valid(self):
        transaction = baker.make(Transaction)

        assert AccountOutputSerializer(transaction.account).data == {
            "id": transaction.account.id,
            "balance": transaction.amount,
        }


@pytest.mark.django_db
class TestAccountMonthlyOutputSerializer:
    def test_valid(self):
        transaction = baker.make(Transaction)
        serializer = AccountMonthlyOutputSerializer(transaction.account)
        serializer.year = transaction.created.year
        serializer.month = transaction.created.month

        assert serializer.data == {
            "id": transaction.account.id,
            "balance": transaction.amount,
            "date": f"{transaction.created.year}-{transaction.created.month:02d}",
        }


class TestAccountInputSerializer:
    input_data = {"year": 2022, "month": 1}

    def test_valid(self):
        serializer = AccountInputSerializer(data=self.input_data)

        assert serializer.is_valid() is True
        assert serializer.validated_data == self.input_data

    def test_available_fields(self):
        assert set(dict(AccountInputSerializer().fields).keys()) == {"month", "year"}

    def test_mandatory_fields(self):
        serializer = AccountInputSerializer(data={})

        assert serializer.is_valid() is False
        assert serializer.errors.keys() == {"year"}

    @pytest.mark.parametrize(
        "month, expected",
        [
            (0, False),
            (1, True),
            (2, True),
            (3, True),
            (4, True),
            (5, True),
            (6, True),
            (7, True),
            (8, True),
            (9, True),
            (10, True),
            (11, True),
            (12, True),
            (13, False),
        ],
    )
    def test_month(self, month, expected):
        serializer = AccountInputSerializer(data={"year": 2022, "month": month})

        assert serializer.is_valid() is expected
