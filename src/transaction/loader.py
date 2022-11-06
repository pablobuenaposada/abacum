import pandas as pd
from django.db import transaction

from transaction.models import Account, Transaction


class Loader:
    @transaction.atomic
    def __init__(self, csv_path):
        df = pd.read_csv(csv_path)
        row_iter = df.iterrows()
        account_instances = []
        transaction_instances = []

        for _, row in row_iter:
            account = Account(id=row["Account"])
            account_instances.append(account)
            transaction_instances.append(
                Transaction(account=account, amount=row["Amount"], created=row["Date"])
            )

        Account.objects.bulk_create(account_instances, ignore_conflicts=True)
        Transaction.objects.bulk_create(transaction_instances)
