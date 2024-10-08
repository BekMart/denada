from django.shortcuts import render
from django.views import generic
from .models import Type, Drink
from home.models import Restaurant

# Create your views here.
def menu_page(request):
    print("About to render template")

    return render(
        request,
        "menu/menu.html",
    )

class DrinkList(generic.ListView):
    queryset = Drink.objects.all().order_by("type")
    template_name = "drink_list.html"
    