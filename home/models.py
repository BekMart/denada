from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    about = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    max_capacity = models.IntegerField()
    num_tables = models.IntegerField()
    restaurant_image = CloudinaryField('image', default='placeholder', blank=True)

    def __str__(self):
        return self.name