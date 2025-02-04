from .models import Booking
from django import forms
from datetime import datetime, date


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('party_size', 'date', 'time', 'special_requests',)

    party_size = forms.IntegerField(widget=forms.NumberInput(attrs={'max': 10}))
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()})
    )

    # Dropdown for time options
    TIME_SLOTS = [(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}") 
                  for hour in range(8, 22) # These are the opening times
                  for minute in (0, 30)] # Display in 30 minute increments
    
    time = forms.ChoiceField(choices=TIME_SLOTS)
    
    special_requests = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('date')
        booking_time_str = cleaned_data.get('time')

        if booking_date is None or booking_time_str is None:
            return cleaned_data

        # Convert time string to time object
        booking_time_obj = datetime.strptime(booking_time_str, "%H:%M").time()

        # Ensure time is not in the past
        current_time = datetime.now()
        if booking_date == current_time.date() and booking_time_obj < current_time.time():
            raise forms.ValidationError("You cannot book a time in the past.")
        
        # Replace the string with the time object for further processing
        cleaned_data['time'] = booking_time_obj

        return cleaned_data


class EditForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('party_size', 'date', 'time', 'special_requests',)

    party_size = forms.IntegerField(widget=forms.NumberInput(attrs={'max': 10}))
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()})
    )

    # Dropdown for time options
    TIME_SLOTS = [(f"{hour:02d}:{minute:02d}", f"{hour:02d}:{minute:02d}") 
                  for hour in range(8, 22)  # These are the opening times
                  for minute in (0, 30)]  # Display in 30 minute increments
    
    time = forms.ChoiceField(choices=TIME_SLOTS)
    
    special_requests = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('date')
        booking_time_str = cleaned_data.get('time')

        if booking_date is None or booking_time_str is None:
            return cleaned_data

        # Convert time string to time object
        booking_time_obj = datetime.strptime(booking_time_str, "%H:%M").time()

        # Ensure time is not in the past
        current_time = datetime.now()
        if booking_date == current_time.date() and booking_time_obj < current_time.time():
            raise forms.ValidationError("You cannot book a time in the past.")
        
        # Replace the string with the time object for further processing
        cleaned_data['time'] = booking_time_obj

        return cleaned_data