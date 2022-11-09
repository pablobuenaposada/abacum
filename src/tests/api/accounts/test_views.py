from django.test import TestCase
from model_bakery import baker
from rest_framework import status
from rest_framework.exceptions import ErrorDetail

from transaction.models import Transaction


class TestAccountViewList(TestCase):
    endpoint = "/api/accounts/"

    def test_valid_only_year(self):
        transaction = baker.make(Transaction)

        response = self.client.get(
            self.endpoint, data={"year": transaction.created.year}
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {"id": transaction.account.id, "balance": transaction.amount},
            ],
        }

    def test_valid_year_and_month(self):
        transaction = baker.make(Transaction)

        response = self.client.get(
            self.endpoint,
            data={"year": transaction.created.year, "month": transaction.created.month},
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {"id": transaction.account.id, "balance": transaction.amount},
            ],
        }


class TestAccountViewDetail(TestCase):
    endpoint = "/api/accounts/"

    def test_valid_only_year(self):
        transaction = baker.make(Transaction)

        response = self.client.get(
            f"{self.endpoint}{transaction.account.id}/",
            data={"year": transaction.created.year},
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": transaction.account.id,
            "balance": transaction.amount,
        }

    def test_valid_year_and_month(self):
        transaction = baker.make(Transaction)

        response = self.client.get(
            f"{self.endpoint}{transaction.account.id}/",
            data={"year": transaction.created.year, "month": transaction.created.month},
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": transaction.account.id,
            "balance": transaction.amount,
        }

    def test_not_found(self):
        response = self.client.get(f"{self.endpoint}666/", data={"year": 2022})

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data == {
            "detail": ErrorDetail(string="Not found.", code="not_found")
        }


class TestAccountMonthlyViewList(TestCase):
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


class TestAccountMonthlyViewDetail(TestCase):
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
