import pytest
from model_bakery import baker

from api.accounts.serializers import AccountOutputSerializer
from transaction.models import Account, Transaction


@pytest.mark.django_db
class TestAccountOutputSerializer:
    def test_valid(self):
        account = baker.make(Account)
        transaction = baker.make(Transaction, account=account)

        assert AccountOutputSerializer(account).data == {
            "id": account.id,
            "balance": transaction.amount,
        }
