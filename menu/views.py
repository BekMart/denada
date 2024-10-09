from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Type, Food, Drink
from home.models import Restaurant

# Create your views here.
def menu_page(request):
    print("About to render template")

    return render(
        request,
        "menu/menu.html",
    )

class FoodList(generic.ListView):
    queryset = Food.objects.all().order_by("type")
    template_name = "menu/food.html"
    context_object_name = 'food_list'


class DrinkList(generic.ListView):
    queryset = Drink.objects.all().order_by("type")
    template_name = "menu/drink.html"
    context_object_name = 'drink_list'
