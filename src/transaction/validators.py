from django.core.exceptions import ValidationError


def validate_amount(value):
    if value == 0:
        raise ValidationError("Amount 0 is not allowed")
    decimals = str(value).split(".")[1:]
    if len(decimals) > 0 and len(decimals[0]) > 2:
        raise ValidationError("No more than 2 decimals allowed")
