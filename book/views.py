from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from .forms import BookingForm
from .models import Booking

# Create your views here.
def booking_page(request):
    booking_form = BookingForm()
    now = timezone.now()

    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(user=request.user, status=0, date__gte=now.date()).order_by('date', 'time')
        # Force re-evaluation of the queryset
        user_bookings = user_bookings.all() 
    else:
        user_bookings = None

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
    

def edit_booking(request, booking_id):
    """
    View for users to edit their bookings
    """
    booking = get_object_or_404(Booking, id=booking_id)
    form = BookingForm()

    if request.method == 'GET':
        booking.status = 1 # Update booking status to 1 - declined
        booking.save() # Update database

        form = BookingForm()  # Create form with initial data
        context = {'form': form, 'booking': booking}
        return render(request, 'book/edit_booking.html', context)

    elif request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()  # Save the updated booking details
            # Redirect to a confirmation page or booking list after successful update
            return redirect('book')  # Replace with your desired redirect URL
        else:
            context = {'form': form, 'booking': booking}
            return render(request, 'book/edit_booking.html', context)

    else:
        return redirect('book')  # Redirect to booking page for invalid requests
