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
    restaurant_image = CloudinaryField('image', default='placeholder', blank=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class About(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_about", default=1
    )
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
    image_1 = CloudinaryField('image', default='placeholder', blank=True)
    image_2 = CloudinaryField('image', default='placeholder', blank=True)
    image_3 = CloudinaryField('image', default='placeholder', blank=True)

class Produce(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_produce", default=1
    )
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
    image_1 = CloudinaryField('image', default='placeholder', blank=True)
    image_2 = CloudinaryField('image', default='placeholder', blank=True)
    image_3 = CloudinaryField('image', default='placeholder', blank=True)

class Visit(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_visit", default=1
    )
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
    image_1 = CloudinaryField('image', default='placeholder', blank=True)
    image_2 = CloudinaryField('image', default='placeholder', blank=True)
    image_3 = CloudinaryField('image', default='placeholder', blank=True)