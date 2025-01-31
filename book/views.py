from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from datetime import timedelta, datetime
from .forms import BookingForm, EditForm
from .models import DiningTable, Booking


def get_user_bookings(user):
    """
    Retrieve future bookings for the authenticated user
    """
    now = timezone.now()
    return Booking.objects.filter(
        user=user, status=0, date__gte=now.date()
    ).order_by('date', 'time')


def get_available_tables(party_size, start_time, end_time):
    """
    Retrieve available tables for a given time period
    """
    return DiningTable.objects.filter(
        seats__gte=party_size
    ).exclude(
        table_booking__start_time__lt=end_time,
        table_booking__end_time__gt=start_time,
    )


def booking_page(request):
    """
    Render booking page
    Display booking form for user to complete
    Display any current bookings that the user has had confirmed
    Assign a table to booking if there is one available 
    Otherwise give feedback and return to booking form
    """
    booking_form = BookingForm()
    user_bookings = get_user_bookings(request.user) if request.user.is_authenticated else None

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            # Extract data from user's booking
            booking_date = booking_form.cleaned_data["date"]
            booking_time = booking_form.cleaned_data["time"]
            party_size = booking_form.cleaned_data["party_size"]

            start_time = datetime.combine(booking_date, booking_time)
            end_time = start_time + timedelta(minutes=60)

            # Get available tables
            available_tables = get_available_tables(party_size, start_time, end_time)

            if available_tables.exists():
                # Create and save the booking
                booking = booking_form.save(commit=False)
                booking.user = request.user
                booking.table = available_tables.first()
                booking.save()

                messages.success(
                    request, "Your booking has been approved! We look forward to seeing you soon."
                )
                return redirect('book')
            else:
                messages.error(
                    request, "No available tables match your booking request.<br> Please try a different time or date."
                )

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
    print('Cancel booking is running')
    booking = Booking.objects.get(pk=booking_id) 

    if request.user == booking.user:  # Check for authentication and ownership
        booking.delete() # Delete record from database
        messages.add_message(request, messages.SUCCESS, 'Your booking has been cancelled!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only cancel your own booking!')

    return redirect('book') # Redirect back to the booking page