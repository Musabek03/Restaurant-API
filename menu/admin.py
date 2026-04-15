from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('category', 'name', 'description', 'price', 'image', 'is_available', 'prep_time', 'created_at', 'updated_at')
    
