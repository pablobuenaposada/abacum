import logging
from datetime import datetime

import pandas as pd
import pytz
from django.db import transaction

from transaction.constants import (LOADER_ACCOUNT_COL, LOADER_AMOUNT_COL,
                                   LOADER_DATE_COL)
from transaction.models import Account, Transaction

logger = logging.getLogger(__name__)


class Loader:
    @transaction.atomic
    def load(self, csv_path):
        df = pd.read_csv(csv_path)
        row_iter = df.iterrows()
        initial_num_accounts = Account.objects.count()
        initial_num_transactions = Transaction.objects.count()
        account_instances = []
        transaction_instances = []

        for _, row in row_iter:
            account = Account(id=row[LOADER_ACCOUNT_COL])
            account_instances.append(account)
            unaware_time = datetime.strptime(row[LOADER_DATE_COL], "%Y-%m-%d")
            aware_time = unaware_time.replace(tzinfo=pytz.UTC)
            transaction_instances.append(
                Transaction(
                    account=account, amount=row[LOADER_AMOUNT_COL], created=aware_time
                )
            )

        Account.objects.bulk_create(account_instances, ignore_conflicts=True)
        transactions_created = Transaction.objects.bulk_create(transaction_instances)
        final_num_accounts = Account.objects.count()
        final_num_transactions = Transaction.objects.count()
        accounts_created = final_num_accounts - initial_num_accounts
        transactions_created = len(transactions_created)

        assert transactions_created == final_num_transactions - initial_num_transactions
        logger.info(
            f"accounts added {accounts_created}, transactions added {transactions_created}"
        )
        return accounts_created, transactions_created
