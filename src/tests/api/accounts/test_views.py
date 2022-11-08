from django.test import TestCase
from model_bakery import baker
from rest_framework import status
from rest_framework.exceptions import ErrorDetail

from transaction.models import Transaction


class TestAccountMonthlyListView(TestCase):
    endpoint = "/api/accounts/monthly/"

    def test_valid(self):
        transactions = baker.make(Transaction, created="2022-01-01", _quantity=2)
        expected = []
        for transaction in transactions:
            for month in range(1, 13):
                expected.append(
                    {
                        "id": transaction.account.id,
                        "balance": transaction.amount,
                        "date": f"2022-{month:02d}",
                    }
                )

        response = self.client.get(self.endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected


class TestAccountMonthlyDetailView(TestCase):
    endpoint = "/api/accounts/monthly/"

    def test_valid(self):
        transaction = baker.make(Transaction, created="2022-01-01")
        expected = []
        for month in range(1, 13):
            expected.append(
                {
                    "id": transaction.account.id,
                    "balance": transaction.amount,
                    "date": f"2022-{month:02d}",
                }
            )
        response = self.client.get(f"{self.endpoint}{transaction.account.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected

    def test_not_found(self):
        response = self.client.get(f"{self.endpoint}666/")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data == {
            "detail": ErrorDetail(string="Not found.", code="not_found")
        }
