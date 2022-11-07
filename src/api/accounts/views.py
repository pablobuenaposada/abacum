from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.accounts.serializers import (AccountInputSerializer,
                                      AccountMonthlyInputSerializer,
                                      AccountMonthlyOutputSerializer,
                                      AccountOutputSerializer)
from transaction.models import Account


class AccountView(ReadOnlyModelViewSet):
    serializer_class = AccountOutputSerializer
    input_serializer = AccountInputSerializer
    queryset = Account.objects.all()

    def retrieve(self, request, *args, **kwargs):
        input_serializer = self.input_serializer(data=request.query_params)
        input_serializer.is_valid(raise_exception=True)
        return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        input_serializer = self.input_serializer(data=request.query_params)
        input_serializer.is_valid(raise_exception=True)
        return super().list(request, *args, **kwargs)


class AccountMonthlyView(ListAPIView):
    serializer_class = AccountMonthlyOutputSerializer
    input_serializer = AccountMonthlyInputSerializer
    queryset = Account.objects.all()

    def list(self, request, *args, **kwargs):
        input_serializer = self.input_serializer(data=request.query_params)
        input_serializer.is_valid(raise_exception=True)
        queryset = self.filter_queryset(self.get_queryset())

        # missing pagination
        by_account = []
        for account in queryset:
            for month in range(1, 13):
                serializer = self.get_serializer(account)
                serializer.month = month
                by_account.append(serializer.data)

        return Response(by_account)
