from .models import Booking
from django import forms
from datetime import datetime

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('party_size', 'date', 'time', 'special_requests',)

    party_size = forms.IntegerField(widget=forms.NumberInput(attrs={'max': 10}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'min': datetime.now().time()}))
    special_requests = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))  # Add rows for multi-line input

class EditForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('party_size', 'date', 'time', 'special_requests',)

    party_size = forms.IntegerField(widget=forms.NumberInput(attrs={'max': 10}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'min': datetime.now().date()}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'min': datetime.now().time()}))
    special_requests = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))  # Add rows for multi-line input