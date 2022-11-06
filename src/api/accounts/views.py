from rest_framework.viewsets import ReadOnlyModelViewSet

from api.accounts.serializers import AccountOutputSerializer
from transaction.models import Account


class AccountView(ReadOnlyModelViewSet):
    serializer_class = AccountOutputSerializer
    queryset = Account.objects.all()
