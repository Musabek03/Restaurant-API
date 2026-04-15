from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('customer', 'table', 'date', 'time', 'guest_count', 'status', 'comment', 'created_at')
    
