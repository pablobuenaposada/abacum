import io

from django.test import TestCase
from rest_framework import status


class TestLoadFileView(TestCase):
    endpoint = "/api/loader/"

    def test_valid(self):
        response = self.client.post(
            self.endpoint,
            data={"file": io.StringIO("Date,Account,Amount\n2020-08-15,1,100")},
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data == {"accounts": 1, "transactions": 1}
