from django.contrib import admin
from .models import MenuItem,Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug', 'is_active')


@admin.register(MenuItem)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('category', 'name', 'description', 'price', 'image', 'is_available', 'prep_time', 'created_at', 'updated_at')
    
