from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone
from .forms import BookingForm, EditForm
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
    View for editing an existing booking.
    """
    booking = Booking.objects.get(pk=booking_id) 

    if request.method == 'POST':
        if request.user == booking.user:  # Check for authentication and ownership
            edit_form = EditForm(data=request.POST, instance=booking) # load editForm
            if edit_form.is_valid(): # check that form is valid
                edit_form.save() # update database
                messages.success(request, 'Booking updated successfully!')
                return redirect('book')  # Redirect back to the booking page
        else:
            messages.error(request, 'You are not authorized to edit this booking.')

    else:
        edit_form = EditForm(data=request.POST)

    return render(request, 'book/edit_booking.html', {'edit_form': edit_form})


def cancel_booking(request, booking_id):
    """
    View for user to delete booking
    """
    booking = Booking.objects.get(pk=booking_id) 

    if request.user == booking.user:  # Check for authentication and ownership
        booking.delete() # Delete record from database
        messages.add_message(request, messages.SUCCESS, 'Your booking has been cancelled!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only cancel your own booking!')

    return redirect('book') # Redirect back to the booking page