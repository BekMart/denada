from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .forms import BookingForm
from .models import Booking

# Create your views here.
def booking_page(request):
    booking_form = BookingForm()
    now = timezone.now()
    user_bookings = Booking.objects.filter(date__gte=now.date())

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Your're booking has been approved! <br> We look forward to seeing you soon!"
            )
            # Redirect to the booking page after successful submission
            return redirect('book') 

    return render(
        request,
        "book/book.html",
        {"booking_form": booking_form, "user_bookings": user_bookings}
    )