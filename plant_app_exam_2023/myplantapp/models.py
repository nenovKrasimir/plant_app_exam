from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


def validate_capitalized_name(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


class Profile(models.Model):
    username = models.CharField(blank=False, unique=True, max_length=10, validators=[MinValueValidator(2)])
    first_name = models.CharField(blank=False, max_length=30, validators=[validate_capitalized_name])
    last_name = models.CharField(blank=False, max_length=30, validators=[validate_capitalized_name])
    profile_picture = models.URLField(blank=True)


class Plant(models.Model):
    plant_type = models.CharField(blank=False, max_length=14)
    name = models.CharField(blank=False, max_length=14)