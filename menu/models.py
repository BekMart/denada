from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    max_capacity = models.IntegerField()
    num_tables = models.IntegerField()
    restaurant_image = CloudinaryField('image', default='placeholder', blank=True)

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)

class Drink(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE ,related_name="drink_types")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    drink_image = CloudinaryField('image', default='placeholder', blank=True)
    calories = models.IntegerField()
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    gluten = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Food(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE ,related_name="food_types")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    food_image = CloudinaryField('image', default='placeholder', blank=True)
    calories = models.IntegerField()
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    gluten = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
