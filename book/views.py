from django.shortcuts import render
from .forms import BookingForm

# Create your views here.
def booking_page(request):
    print("About to render template")
    booking_form = BookingForm()

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()

    return render(
        request,
        "book/book.html",
        {"booking_form": booking_form,}
    )