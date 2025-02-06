from django.db import models
from home.models import Restaurant
from cloudinary.models import CloudinaryField

"""
Models for the Menu app.
This module defines models for managing restaurant menus, including:
- Menu: Stores general menu information.
- Type: Represents categories for food and drink items.
- Food: Represents individual food items.
- Drink: Represents individual drink items.
"""


class Menu(models.Model):
    """
    Represents a restaurant's menu page details.
    - restaurant (FK): Links the menu to a specific restaurant.
    - title (CharField): The title of the main menu page.
    - about (TextField): A short description of the menu.
    - menu_image (CloudinaryField): An optional image for the main menu page.
    - note (TextField): Additional notes related to the menu.
    - updated_on (DateTimeField): Timestamp of the last update.
    """
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    about = models.TextField(blank=True)
    menu_image = CloudinaryField('image', default='placeholder', blank=True)
    note = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now_add=True)


class Type(models.Model):
    """
    Represents a category or type of food or drink item.
    - name (CharField): The name of the type (e.g., Breakfast, Hot Drinks).
    - slug (SlugField): A URL-friendly version of the name.
    - description (TextField): A description of the type.
    - type_image (CloudinaryField): An optional image for the type.
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    type_image = CloudinaryField('image', default='placeholder', blank=True)

    def __str__(self):
        """String representation of the food or drink type."""
        return self.name


class Drink(models.Model):
    """
    Represents an individual drink item on the menu.
    - name (CharField): The name of the drink.
    - slug (SlugField): A URL-friendly version of the name.
    - type (FK): The category of the drink, linked to the Type model.
    - description (TextField): A short description of the drink.
    - price (DecimalField): The price of the drink.
    - drink_image (CloudinaryField): An optional image of the drink.
    - calories (IntegerField): The number of calories in the drink.
    - vegetarian (BooleanField): Indicates if the drink is vegetarian-friendly.
    - vegan (BooleanField): Indicates if the drink is vegan-friendly.
    - gluten (BooleanField): Indicates if the drink is gluten-free.
    - restaurant (FK): Links the drink to a specific restaurant.
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="drink_types")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    drink_image = CloudinaryField('image', default='placeholder', blank=True)
    calories = models.IntegerField()
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    gluten = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the drink - its name."""
        return self.name


class Food(models.Model):
    """
    Represents an individual food item on the menu.
    - name (CharField): The name of the food item.
    - slug (SlugField): A URL-friendly version of the name.
    - type (FK): The category of the food, linked to the Type model.
    - description (TextField): A short description of the food item.
    - price (DecimalField): The price of the food item.
    - food_image (CloudinaryField): An optional image of the food item.
    - calories (IntegerField): The number of calories in the food item.
    - vegetarian (BooleanField): Indicates if the food is vegetarian-friendly.
    - vegan (BooleanField): Indicates if the food is vegan-friendly.
    - gluten (BooleanField): Indicates if the food is gluten-free.
    - restaurant (FK): Links the food item to a specific restaurant.
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="food_types")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    food_image = CloudinaryField('image', default='placeholder', blank=True)
    calories = models.IntegerField()
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    gluten = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the food - its name."""
        return self.name
