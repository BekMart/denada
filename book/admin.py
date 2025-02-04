from django.contrib import admin
from .models import Booking, STATUS

# # Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('user', 'restaurant', 'party_size', 'date', 'time', 'status', 'id', 'table')
    search_fields = ['user', 'restaurant']
    list_filter = ('restaurant', 'user', 'date', 'time', 'status')

    def get_status_display(self, obj):
        return STATUS[obj.status][1]  # Access the second element (string value)