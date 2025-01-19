from django.db import models
from django.contrib.auth.models import User
from home.models import Restaurant
from cloudinary.models import CloudinaryField

# Create your models here.
class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    about = models.TextField(blank=True)
    menu_image = CloudinaryField('image', default='placeholder', blank=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant.name

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    type_image = CloudinaryField('image', default='placeholder', blank=True)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name
