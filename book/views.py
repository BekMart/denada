from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def booking_page(request):
    print("About to render template")

    return render(
        request,
        "book/book.html",
    )