from django.contrib import admin
from .models import Table


@admin.register(Table)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('number', 'capacity', 'location', 'is_active')
    
