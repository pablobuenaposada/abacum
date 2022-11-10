from contextlib import nullcontext as does_not_raise

import pytest
from django.core.exceptions import ValidationError

from transaction.validators import validate_amount


class TestValidateAmount:
    @pytest.mark.parametrize(
        "value, expectation",
        [
            (1, does_not_raise()),
            (1.0, does_not_raise()),
            (1.11, does_not_raise()),
            (-1, does_not_raise()),
            (1.111, pytest.raises(ValidationError)),  # too many decimals
            (0, pytest.raises(ValidationError)),
        ],
    )
    def test_validate_amount(self, value, expectation):
        with expectation:
            validate_amount(value)
