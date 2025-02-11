from django.shortcuts import render
from django.views import generic
from .models import Menu, Food, Drink


def menu_page(request):
    """
    Renders the menu page with the latest menu details.
    - Takes the incoming request object.
    - Renturns the most recently updated records of the menu details
    and passes it to the template.
    """
    # Retrieve the latest updated menu details
    latest_menu = Menu.objects.latest('updated_on')

    # Context dictionary to pass data to the template
    context = {
        'menu': latest_menu,
    }

    # Render and return the menu page with the latest menu details
    return render(
        request,
        "menu/menu.html",
        context
    )


class FoodList(generic.ListView):
    """
    Displays a list of Food items.
    - Retrieves all Food objects ordered by their type.
    - Renders the context_object_name to the template_name address.
    """
    # Order food by type name instead of type ID
    queryset = Food.objects.all().order_by("type")
    template_name = "menu/food.html"  # The file path of where to display list
    context_object_name = 'food_list'  # List to be sent


class DrinkList(generic.ListView):
    """
    Displays a list of Drink items.
    - Retrieves all Food objects ordered by their type.
    - Renders the context_object_name to the template_name address.
    """
    # Order drinks by type name instead of type ID
    queryset = Drink.objects.all().order_by("type")
    template_name = "menu/drink.html"  # The file path of where to display list
    context_object_name = 'drink_list'  # List to be sent
