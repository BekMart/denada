from .models import Booking
from django import forms
from datetime import datetime, date


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('party_size', 'date', 'time', 'special_requests')

    party_size = forms.IntegerField(widget=forms.NumberInput(attrs={'max': 10}))
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()})
    )
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    special_requests = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('date')
        booking_time = cleaned_data.get('time')

        if booking_date is None or booking_time is None:
            return cleaned_data

        # Ensure time is not in the past for today's bookings
        current_time = datetime.now()
        if booking_date == current_time.date() and booking_time < current_time.time():
            raise forms.ValidationError("You cannot book a time in the past.")

        return cleaned_data


class EditForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('party_size', 'date', 'time', 'special_requests',)

    party_size = forms.IntegerField(widget=forms.NumberInput(attrs={'max': 10}))
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()})
    )
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    special_requests = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('date')
        booking_time = cleaned_data.get('time')

        if booking_date is None or booking_time is None:
            return cleaned_data

        # Ensure time is not in the past for today's bookings
        current_time = datetime.now()
        if booking_date == current_time.date() and booking_time < current_time.time():
            raise forms.ValidationError("You cannot book a time in the past.")

        return cleaned_data