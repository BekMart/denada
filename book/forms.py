from django import forms
from datetime import datetime, date
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Form for creating a new booking.
    This form allows users to book a table by specifying the number of guests,
    date, time and any special requests.
    It also includes validation to ensure that past times cannot be selected.
    """

    class Meta:
        """
        Meta class defining model and fields for the form.
        """
        model = Booking
        fields = ('party_size', 'date', 'time', 'special_requests',)

    # Integer field for party size (must be between 1 - 10)
    party_size = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1, 'max': 10}))

    # Date field (must be today or after)
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()})
    )

    # Dropdown selection for time slots in 30-minute increments between 08:00-21:30
    TIME_SLOTS = [(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}")
                  for hour in range(8, 22)  # These are the opening times
                  for minute in (0, 30)]  # Display in 30 minute increments

    time = forms.ChoiceField(choices=TIME_SLOTS)

    # Optional text field for user to add special requests
    special_requests = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))

    def clean(self):
        """
        Custom validation for the booking form
        - Ensures that selected time is not in the past.
        - Converts time from string to time bject for further processing.
        - Returns dictionary of cleaned data.
        """
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('date')
        booking_time_str = cleaned_data.get('time')

        # If date or time is not provided, return the data as-is
        if booking_date is None or booking_time_str is None:
            return cleaned_data

        # Convert the selected time from string to time object
        booking_time_obj = datetime.strptime(booking_time_str, "%H:%M").time()

        # Get the current date and time
        current_time = datetime.now()

        # Ensure users cannot select a time that has already passed today
        if booking_date == current_time.date() and booking_time_obj < current_time.time():
            self.add_error('time', "You cannot book a time in the past.")

        # Replace string time with time object for further processing
        cleaned_data['time'] = booking_time_obj

        return cleaned_data


class EditForm(forms.ModelForm):
    """
    Form for editing an existing booking.
    This forms allows users to update their existing booking details,
    including the number of guests, date, time and special requests.
    """

    class Meta:
        """
        Meta class defining model and fields for the form.
        """
        model = Booking
        fields = ('party_size', 'date', 'time', 'special_requests',)

    # Integer field for party size (must be between 1 - 10)
    party_size = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1, 'max': 10}))

    # Date field (must be today or after)
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()})
    )

    # Dropdown selection for time slots in 30-minute increments between 08:00-21:30
    TIME_SLOTS = [(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}") 
                  for hour in range(8, 22)  # These are the opening times
                  for minute in (0, 30)]  # Display in 30 minute increments

    time = forms.ChoiceField(choices=TIME_SLOTS)

    # Optional text field for user to add special requests
    special_requests = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))

    def clean(self):
        """
        Custom validation for the booking form
        - Ensures that selected time is not in the past.
        - Converts time from string to time bject for further processing.
        - Returns dictionary of cleaned data.
        """
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('date')
        booking_time_str = cleaned_data.get('time')

        # If date or time is not provided, return the data as-is
        if booking_date is None or booking_time_str is None:
            return cleaned_data

        # Convert the selected time from string to time object
        booking_time_obj = datetime.strptime(booking_time_str, "%H:%M").time()

        # Get the current date and time
        current_time = datetime.now()

        # Ensure users cannot select a time that has already passed today
        if booking_date == current_time.date() and booking_time_obj < current_time.time():
            self.add_error('time', "You cannot book a time in the past.")

        # Replace string time with time object for further processing
        cleaned_data['time'] = booking_time_obj

        return cleaned_data
