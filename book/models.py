from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import is_naive, make_aware
from datetime import timedelta, datetime
from home.models import Restaurant

# Status choices for booking confirmation
STATUS = ((0, "Confirmed"), (1, "Declined"))


class DiningTable(models.Model):
    """
    Model representing the individual tables within a restaurant.
    - restaurant (FK): The restaurant to which the table belongs.
    - seats (PositiveIntegerField): Number of seats available at the table.
    """
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="restaurant_table",
        default=1
    )
    seats = models.PositiveIntegerField()

    def __str__(self):
        """String representation of the table."""
        return f"Table {self.id} at {self.restaurant} with {self.seats} seats"


class Booking(models.Model):
    """
    Model representing table booking.
    - user (FK): The user who made the booking.
    - restaurant (FK): The restaurant where the booking is made.
    - table (FK): The specific table booked.
    - party_size (PositiveIntegerField): Number of guests for the booking.
    - date (DateField): Date of the booking.
    - time (TimeField): Time of the booking.
    - created_on (DateTimeField): Timestamp when the booking was created.
    - special_requests (TextField): Optional field for special requests.
    - status (IntegerField): Status of the booking (Confirmed/Declined).
    - start_time (DateTimeField): Computed datetime when the booking starts.
    - end_time (DateTimeField): Computed datetime when the booking ends.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_booking"
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="restaurant_booking",
        default=1
    )
    table = models.ForeignKey(
        DiningTable, on_delete=models.CASCADE, related_name="table_booking"
    )
    party_size = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    special_requests = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        """
        Custom save method to set start_time and end_time automatically.
        - start_time is set based on the provided date and time.
        - end_time is calculated as one hour after start_time.
        """
        # The date and time of the booking
        booking_datetime = datetime.combine(self.date, self.time)

        # Ensure the datetime is timezone-aware
        if is_naive(booking_datetime):
            booking_datetime = make_aware(booking_datetime)

        self.start_time = booking_datetime  # Assign value to strat time
        # Assign value to end time - 1 hour after start time
        self.end_time = self.start_time + timedelta(minutes=60)

        # Call the parent class's save method to save object to database
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["date", "time"]  # Order bookings by date and time

    def __str__(self):
        """String representation of the booking."""
        return (
            f"Booking for {self.restaurant} |
            {self.party_size} guests |
            {self.date} |
            {self.time} |
            {self.get_status_display()}"
        )
