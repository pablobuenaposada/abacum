from rest_framework import serializers

from transaction.models import Account


class AccountOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "balance"]
