from rest_framework.viewsets import ReadOnlyModelViewSet

from api.accounts.serializers import (AccountInputSerializer,
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
