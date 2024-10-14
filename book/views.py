from django.shortcuts import render
from .forms import BookingForm

# Create your views here.
def booking_page(request):
    print("About to render template")
    booking_form = BookingForm()

    return render(
        request,
        "book/book.html",
        {"booking_form": booking_form,}
    )