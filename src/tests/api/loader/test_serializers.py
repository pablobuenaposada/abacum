import tempfile

from api.loader.serializers import (FileUploadInputSerializer,
                                    FileUploadOutputSerializer)


class TestFileUploadInputSerializer:
    def test_valid(self):
        fp = tempfile.NamedTemporaryFile(suffix=".csv")
        serializer = FileUploadInputSerializer(data={"file": fp})
        serializer.is_valid(raise_exception=True)


class TestFileUploadOutputSerializer:
    def test_valid(self):
        assert FileUploadOutputSerializer({"accounts": 1, "transactions": 1}).data == {
            "accounts": 1,
            "transactions": 1,
        }
