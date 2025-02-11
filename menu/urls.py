from . import views
from django.urls import path

# Define URL patterns for the menu app
urlpatterns = [
    path('', views.menu_page, name='menu'),  # Route for main menu page
    path('food/', views.FoodList.as_view(), name='food'),  # Food menu page
    path('drink/', views.DrinkList.as_view(), name='drink'),  # Drink menu page
]
