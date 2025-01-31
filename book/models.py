from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import is_naive, make_aware
from datetime import timedelta, datetime
from home.models import Restaurant

STATUS = ((0, "Confirmed"), (1, "Declined"))


# Create your models here.
class DiningTable(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_table", default=1
    )
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"Table at {self.restaurant} with {self.seats} seats"
    

class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_booking"
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_booking", default=1
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
        # Automatically set start_time and end_time
        booking_datetime = datetime.combine(self.date, self.time)
        
        if is_naive(booking_datetime):
            booking_datetime = make_aware(booking_datetime)

        self.start_time = booking_datetime
        self.end_time = self.start_time + timedelta(minutes=60)
        
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Booking for {self.restaurant} | {self.party_size} guests | {self.date} | {self.time} | {self.get_status_display()}"