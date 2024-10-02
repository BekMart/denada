from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menu_page(request):
    return HttpResponse("TAKE A LOOK AT OUR MENUS!")