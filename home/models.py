from django.db import models
from cloudinary.models import CloudinaryField

"""
Models for the Home app.
This module defines models for storing restaurant-related information,
including general details, an about section, produce information,
and reasons to visit.
"""


class Restaurant(models.Model):
    """
    Represents a restaurant.
    - name (CharField): The name of the restaurant.
    - slug (SlugField): A URL-friendly slug generated from the restaurant name.
    - address (CharField): The restaurant's physical address.
    - phone (CharField): The restaurant's contact phone number.
    - email (EmailField): The restaurant's contact email.
    - restaurant_image (CloudinaryField): A hero image for the website.
    - updated_on (DateTimeField): Timestamp of the last update.
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    # Changed to Charfield to enable styling via summernote
    email = models.CharField(max_length=255)
    restaurant_image = CloudinaryField(
        'image', default='placeholder', blank=True
        )
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the Restaurant table."""
        return self.name


class About(models.Model):
    """
    Represents the About section of a restaurant.
    - restaurant (FK): Links the about section to a restaurant.
    - title (CharField): The title of the about section.
    - content (TextField): The main content of the about section.
    - updated_on (DateTimeField): Timestamp of the last update.
    - image_1, image_2, image_3 (CloudinaryField): Images associated with the
    about section.
    """
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="restaurant_about",
        default=1
    )
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
    image_1 = CloudinaryField('image', default='placeholder', blank=True)
    image_2 = CloudinaryField('image', default='placeholder', blank=True)
    image_3 = CloudinaryField('image', default='placeholder', blank=True)


class Produce(models.Model):
    """
    Represents produce-related information for a restaurant.
    - restaurant (FK): Links the produce entry to a restaurant.
    - title (CharField): The title of the produce section.
    - content (TextField): The main content of the produce section.
    - updated_on (DateTimeField): Timestamp of the last update.
    - image_1, image_2, image_3 (CloudinaryField): Images associated with
    the produce.
    """
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="restaurant_produce",
        default=1
    )
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
    image_1 = CloudinaryField('image', default='placeholder', blank=True)
    image_2 = CloudinaryField('image', default='placeholder', blank=True)
    image_3 = CloudinaryField('image', default='placeholder', blank=True)


class Visit(models.Model):
    """
    Represents reasons to visit section for a restaurant.
    - restaurant (FK): Links the visit section to a restaurant.
    - title (CharField): The title of the visit section.
    - content (TextField): The main content of the visit section for
    the restaurant.
    - updated_on (DateTimeField): Timestamp of the last update.
    - image_1, image_2, image_3 (CloudinaryField): Images associated with
    the visit section.
    """
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="restaurant_visit",
        default=1
    )
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
    image_1 = CloudinaryField('image', default='placeholder', blank=True)
    image_2 = CloudinaryField('image', default='placeholder', blank=True)
    image_3 = CloudinaryField('image', default='placeholder', blank=True)
