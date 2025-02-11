from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta, datetime
from .forms import BookingForm, EditForm
from .models import DiningTable, Booking


def get_user_bookings(user):
    """
    Retrieve existing bookings for the authenticated user.
    - Takes the authenticated user as an arguement.
    - Returns a list of future bookings, order by date and time.
    """
    now = timezone.now()  # Get the current date and time in local timezone
    return Booking.objects.filter(
        user=user,  # Only show objects that are associated with the user
        status=0,  # Only show confirmed bookings
        date__gte=now.date()  # Only show today and future dates
    ).order_by('date', 'time')  # Order list by date and time


def get_available_tables(party_size, start_time, end_time):
    """
    Retrieve available tables for a given time period.
    - Takes the party size and the start and end time of the booking.
    - Return a list of tables that are available.
    """
    return DiningTable.objects.filter(
        seats__gte=party_size  # Tables with seats >= party size
    ).exclude(
        # Exclude tables that are already booked during the requested time slot
        table_booking__start_time__lt=end_time,  # starts before the end_time
        table_booking__end_time__gt=start_time,  # ends after the start_time
    )


def booking_page(request):
    """
    Handle booking page display and processing.
    - Takes the HTTP request object.
    - Assigns a table to booking if there is one available.
    - Feedback provided if booking is successful or declined.
    - Returns rendered template with the booking form and list of
    users existing bookings.
    """
    # Initialise an empty booking form
    booking_form = BookingForm()
    # Retrieve user's exsting bookings if they are authenticated
    if request.user.is_authenticated:
        user_bookings = get_user_bookings(request.user)
    else:
        user_bookings = None

    if request.method == "POST":  # Handle form submission
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():  # Validate form data
            # Extract cleaned data from the form
            booking_date = booking_form.cleaned_data["date"]
            booking_time = booking_form.cleaned_data["time"]
            party_size = booking_form.cleaned_data["party_size"]

            # Combine date and timme to form a datetime object
            start_time = datetime.combine(booking_date, booking_time)
            end_time = start_time + timedelta(minutes=60)  # 1 hour slot

            # Get available tables for the selected time and party size
            available_tables = get_available_tables(
                party_size,
                start_time,
                end_time
                )

            if available_tables.exists():  # If available table, create booking
                # Do not save yet, assign user and table first
                booking = booking_form.save(commit=False)
                # Assign booking to authenticated user
                booking.user = request.user
                # Assign first available table
                booking.table = available_tables.first()
                booking.save()  # Save the booking to the database
                # Feedback provided
                messages.success(
                    request,
                    "Your booking has been approved!<br>\
                    We look forward to seeing you soon."
                )
                return redirect('book')  # Redirect to booking page
            else:
                messages.error(
                    request,
                    "No available tables match your booking request.<br>\
                    Please try a different time or date."
                )

    # Render the booking page with the booking form and user's bookings
    return render(
        request,
        "book/book.html",
        {"booking_form": booking_form, "user_bookings": user_bookings}
    )


def edit_booking(request, booking_id):
    """
    View to edit an existing booking.
    - Takes the HTTP request and booking ID.
    - Displays the edit form pre-populated with booking details.
    - Validates and updates the booking if user is authenticated.
    - Returns rendered edit booking page or redirect on success.
    """
    # Get the booking object, or return 404 if it doesn't exist
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == 'POST':
        if request.user == booking.user:  # Ensure the user owns the booking
            edit_form = EditForm(
                data=request.POST,
                instance=booking)  # Load the form with POST data
            if edit_form.is_valid():  # Validate the form
                edit_form.save()  # Save changes to the database
                messages.success(request, 'Booking updated successfully!')
                return redirect('book')  # Redirect back to the booking page
            else:
                messages.error(
                    request,
                    "No available tables match your booking request.<br>\
                    Please try a different time or date."
                )
        else:
            messages.error(
                request,
                'You are not authorised to edit this booking.'
                )
            return redirect('book')  # Redirect unauthorised users to book page
    else:
        # Load form pre-filled with the existing booking data for GET requests
        edit_form = EditForm(instance=booking)

    # Render the template with the form
    return render(
        request,
        'book/edit_booking.html',
        {'edit_form': edit_form}
    )


def cancel_booking(request, booking_id):
    """
    View to cancel a user's booking.
    - Takes the HTTP request and booking ID.
    - Feedback given to user.
    - Redirects to booking page after cancellation.
    """
    booking = Booking.objects.get(pk=booking_id)

    if request.user == booking.user:  # Ensure the user owns the booking
        booking.delete()  # Delete record of booking from database
        messages.add_message(
            request, messages.SUCCESS,
            'Your booking has been cancelled!'
            )
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only cancel your own booking!'
            )

    return redirect('book')  # Redirect back to the booking page
