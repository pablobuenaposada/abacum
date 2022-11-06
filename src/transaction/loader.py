from datetime import datetime

import pandas as pd
import pytz
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
            unaware_time = datetime.strptime(row["Date"], "%Y-%m-%d")
            aware_time = unaware_time.replace(tzinfo=pytz.UTC)
            transaction_instances.append(
                Transaction(account=account, amount=row["Amount"], created=aware_time)
            )

        Account.objects.bulk_create(account_instances, ignore_conflicts=True)
        Transaction.objects.bulk_create(transaction_instances)
