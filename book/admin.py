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


class DiningTableAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'id', 'seats', 'get_bookings')

    def get_bookings(self, obj):
        """Retrieve all bookings associated with this table."""
        # All bookings related to table
        table_booking = obj.table_booking.all()
        if table_booking.exists():
            return ", ".join(
                [f"#{b.id} ({b.date} {b.time})" for b in table_booking])
        return "No bookings"

    get_bookings.short_description = "Bookings"  # Column name in Admin


admin.site.register(DiningTable, DiningTableAdmin)
