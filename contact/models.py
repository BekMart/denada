from django.db import models
from home.models import Restaurant

"""
Models for storing contact-related information for a restaurant.
This module defines models for managing restaurant-related details, including:
- Time: Stores business hours.
- Address: Stores restaurant addresses.
- Contact: Stores general contact information.
- Social: Stores social media links.
"""


class Time(models.Model):
    """
    Represents business hours for a restaurant.
    - restaurant (FK): The restaurant the opening times are associated with.
    - title (CharField): A short name fr the time entry.
    - time_list (TextField): Detailed business hours (summernote - rich text).
    - updated_on (DateTimeField): Timestamp of the last update.
    """
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="restaurant_times",
        default=1
    )
    title = models.CharField(max_length=50, unique=True)
    time_list = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the Time table."""
        return self.title


class Address(models.Model):
    """
    Represents a restaurant's address.
    - restaurant (FK): Links the address entry to a specific restaurant.
    - title (CharField): A short title for the address.
    - updated_on (DateTimeField): Timestamp of the last update.
    """
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="restaurant_address",
        default=1
    )
    title = models.CharField(max_length=50, unique=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the Address table."""
        return self.title


class Contact(models.Model):
    """
    Represents a restaurant's contact information.
    - restaurant (FK): Links the contact entry to a specific restaurant.
    - title (CharField): A short title for the contact information.
    - updated_on (DateTimeField): Timestamp of the last update.
    """
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="restaurant_contact",
        default=1
    )
    title = models.CharField(max_length=50, unique=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the Contact table."""
        return self.title


class Social(models.Model):
    """
    Represents a restaurant's social media accounts.
    - restaurant (FK): Links the social media accounts a specific restaurant.
    - title (CharField): A short title for the social media information.
    - facebook (CharField): The restaurant's Facebook profile link.
    - instagram (CharField): The restaurant's Instagram profile link.
    - twitter (CharField): The restaurant's Twitter profile link.
    -  updated_on (DateTimeField): Timestamp of the last update.
    """
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="restaurant_socials",
        default=1
    )
    title = models.CharField(max_length=50, unique=True)
    facebook = models.CharField(max_length=350)
    instagram = models.CharField(max_length=350)
    twitter = models.CharField(max_length=350)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the Contact table."""
        return self.title
