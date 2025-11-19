from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model that extends the built-in User model
    with additional information like favorite city.
    """
    #: Link to the Django User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    #: User's favorite city (optional)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self) -> str:
        """
        Return the username associated with this profile.

        Returns:
            str: Username of the linked user.
        """
        return self.user.username
