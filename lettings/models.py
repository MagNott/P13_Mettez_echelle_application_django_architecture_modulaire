from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address linked to a letting.

    Stores structured data for the street, city, and postal information.
    Each address is unique and associated with a single letting.
    """
    class Meta:
        verbose_name_plural = "addresses"

    #: Street number (max 4 digits)
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])

    #: Street name (up to 64 characters)
    street = models.CharField(max_length=64)

    #: City name (up to 64 characters)
    city = models.CharField(max_length=64)

    #: Two-letter state abbreviation (e.g., 'CA')
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])

    #: Postal code (max 5 digits)
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])

    #: Three-letter country code (ISO 3166-1 alpha-3)
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self) -> str:
        """
        Returns a readable string representation of the address.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Represents a property available for rent.

    Each letting is linked to a unique address and has a descriptive title
    to identify the property in the interface.
    """
    #: Name or label of the property
    title = models.CharField(max_length=256)

    #: One-to-one relationship to the property's address
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """
        Returns a readable string representation of the letting.
        """
        return self.title
