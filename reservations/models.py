from django.db import models
from accounts.models import CustomUser
from menu.models import Category, MenuItem
from tables.models import Table

class Reservation(models.Model):

    STATUS_CHOICES =  ( 
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed") )


    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="reservations")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reservations")
    date = models.DateField()
    time = models.TimeField()
    guest_count = models.PositiveBigIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    comment = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.customer} - {self.date} {self.time}"
    