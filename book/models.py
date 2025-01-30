from django.db import models
from django.contrib.auth.models import User
from home.models import Restaurant

STATUS = ((0, "Confirmed"), (1, "Declined"))


# Create your models here.
class DiningTable(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_table", default=1
    )
    seats = models.IntegerField()

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
        DiningTable, on_delete=models.CASCADE, related_name="table_booking", null=True, blank=True
    )
    party_size = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    special_requests = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Booking for {self.restaurant} | {self.party_size} guests | {self.date} | {self.time} | {self.get_status_display()}"
