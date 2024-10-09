from django.shortcuts import render
from django.views import generic
from .models import Type, Food, Drink
from home.models import Restaurant

# Create your views here.
class FoodList(generic.ListView):
    queryset = Food.objects.all().order_by("type")
    template_name = "menu/menu.html"

class DrinkList(generic.ListView):
    queryset = Drink.objects.all().order_by("type")
    template_name = "menu/menu.html"

