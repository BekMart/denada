from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def booking_page(request):
    return HttpResponse("BOOK A TABLE HERE!")