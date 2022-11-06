from rest_framework import serializers


class FileUploadInputSerializer(serializers.Serializer):
    file = serializers.FileField()


class FileUploadOutputSerializer(serializers.Serializer):
    accounts = serializers.IntegerField()
    transactions = serializers.IntegerField()
