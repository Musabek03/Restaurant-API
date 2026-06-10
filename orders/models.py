from django.db import models
from accounts.models import CustomUser
from tables.models import Table
from reservations.models import Reservation
from menu.models import MenuItem

STATUS_CHOICES = (
    ('new', 'New'),
    ('in_progress', 'In_progress'),
    ('ready', 'Ready'),
    ('served', 'Served'),
    ('cancelled', 'Cancelled')
)



class Order(models.Model):

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.email or self.customer.username}"


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.RESTRICT, related_name='orderitems')
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} (Order #{self.order.id})"