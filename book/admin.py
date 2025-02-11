from django.contrib import admin
from .models import Booking, STATUS, DiningTable


# Register booking models with custom admin settings
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Booking model.
    This class customizes the Django admin interface for the Booking model,
    allowing easier management of bookings via list display,
    filtering, and searching.
    """
    list_display = (
        'user',
        'restaurant',
        'date',
        'time',
        'party_size',
        'table',
        'status',
        'id'
        )
    search_fields = ['user__username', 'date', 'time']
    list_filter = ('restaurant', 'user', 'date')

    def get_status_display(self, obj):
        """
        Retrieve the human-readable status label from the STATUS choices.
        Takes the booking instance as an arguement.
        Returns a string value to display label of status.
        """
        return STATUS[obj.status][1]  # Access the second element


@admin.register(DiningTable)
class DiningTableAdmin(admin.ModelAdmin):
    """
    Admin configuration for the DiningTable model.
    This class customizes the Django admin interface for DiningTable,
    making it easier to manage bookings with associated tables.
    """
    list_display = ('restaurant', 'id', 'seats')
