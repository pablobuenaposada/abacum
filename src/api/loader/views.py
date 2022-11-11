from rest_framework import generics, status
from rest_framework.response import Response

from api.loader.serializers import (FileUploadInputSerializer,
                                    FileUploadOutputSerializer)
from transaction.loader import Loader


class LoadFileView(generics.CreateAPIView):
    serializer_class = FileUploadInputSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        num_accounts, num_transactions = Loader().load(request.data["file"].file)
        return Response(
            FileUploadOutputSerializer(
                {"accounts": num_accounts, "transactions": num_transactions}
            ).data,
            status.HTTP_201_CREATED,
        )
