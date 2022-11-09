from django.core.files.uploadedfile import TemporaryUploadedFile

from api.loader.serializers import (FileUploadInputSerializer,
                                    FileUploadOutputSerializer)


class TestFileUploadInputSerializer:
    def test_valid(self):
        file = TemporaryUploadedFile("foo", None, 1, None)
        serializer = FileUploadInputSerializer(data={"file": file})

        assert serializer.is_valid() is True

    def test_available_fields(self):
        assert set(dict(FileUploadInputSerializer().fields).keys()) == {"file"}

    def test_mandatory_fields(self):
        serializer = FileUploadInputSerializer(data={})

        assert serializer.is_valid() is False
        assert serializer.errors.keys() == {"file"}


class TestFileUploadOutputSerializer:
    def test_valid(self):
        assert FileUploadOutputSerializer({"accounts": 1, "transactions": 1}).data == {
            "accounts": 1,
            "transactions": 1,
        }
