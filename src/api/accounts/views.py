from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.accounts.serializers import (AccountInputSerializer,
                                      AccountMonthlyOutputSerializer,
                                      AccountOutputSerializer)
from transaction.models import Account


class AccountView(ReadOnlyModelViewSet):
    serializer_class = AccountOutputSerializer
    input_serializer = AccountInputSerializer
    queryset = Account.objects.all()

    def _validate_params(self, request):
        input_serializer = self.input_serializer(data=request.query_params)
        input_serializer.is_valid(raise_exception=True)

    def retrieve(self, request, *args, **kwargs):
        self._validate_params(request)
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self._validate_params(request)
        return super().list(request, *args, **kwargs)


class AccountMonthlyView(ReadOnlyModelViewSet):
    serializer_class = AccountMonthlyOutputSerializer
    queryset = Account.objects.all()

    def _get_account_monthly_balance(self, years, instance):
        results = []
        for year in years:
            for month in range(1, 13):
                serializer = self.get_serializer(instance)
                serializer.year = year
                serializer.month = month
                results.append(serializer.data)
        return results

    def retrieve(self, request, *args, **kwargs):
        account = self.get_object()
        years = [date.year for date in account.transaction_set.dates("created", "year")]
        return Response(self._get_account_monthly_balance(years, account))

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # missing pagination
        results = []
        for account in queryset:
            years = [
                date.year for date in account.transaction_set.dates("created", "year")
            ]
            results.extend(self._get_account_monthly_balance(years, account))
        return Response(results)
