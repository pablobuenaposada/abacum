from rest_framework import serializers

from transaction.models import Account


class AccountOutputSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ["id", "balance"]

    def get_balance(self, obj):
        try:
            year = self.context["request"].query_params.get("year", None)
        except KeyError:
            year = None

        try:
            month = self.context["request"].query_params.get("month", None)
        except KeyError:
            month = None

        return obj.balance(year, month)


class AccountInputSerializer(serializers.Serializer):
    year = serializers.IntegerField(required=False)
    month = serializers.IntegerField(required=False, min_value=1, max_value=12)
