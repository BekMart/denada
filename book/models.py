from django.db import models
from django.contrib.auth.models import User
from home.models import Restaurant

STATUS = ((0, "Pending"), (1, "Confirmed"), (2, "Declined"))

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_booking"
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="restaurant_booking"
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
        return f"Booking for {self.restaurant} | {self.party_size} guests | {self.date} | {self.time} | {self.status}"