from django.core.exceptions import ValidationError


def validate_amount(value):
    if value == 0:
        raise ValidationError("Amount 0 is not allowed")
