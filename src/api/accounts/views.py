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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        years = [
            date.year for date in instance.transaction_set.dates("created", "year")
        ]

        results = []
        for year in years:
            for month in range(1, 13):
                serializer = self.get_serializer(instance)
                serializer.year = year
                serializer.month = month
                results.append(serializer.data)

        return Response(results)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # missing pagination
        results = []
        for account in queryset:
            years = [
                date.year for date in account.transaction_set.dates("created", "year")
            ]
            for year in years:
                for month in range(1, 13):
                    serializer = self.get_serializer(account)
                    serializer.year = year
                    serializer.month = month
                    results.append(serializer.data)

        return Response(results)
