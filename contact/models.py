from django.db import models
from home.models import Restaurant

# Create your models here.
class OpeningTime(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_times", default=1
    )
    title = models.CharField(max_length=50, unique=True)
    time_list = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Address(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_address", default=1
    )
    title = models.CharField(max_length=50, unique=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_contact", default=1
    )
    title = models.CharField(max_length=50, unique=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Social(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_socials", default=1
    )
    title = models.CharField(max_length=50, unique=True)
    app = models.CharField(max_length=255)
    updated_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title