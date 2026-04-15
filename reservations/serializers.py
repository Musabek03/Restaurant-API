from rest_framework import serializers
from .models import Reservation



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'customer', 'table', 'date', 'time', 
                'guest_count', 'status', 'comment', 'created_at']
        read_only_fields = ['created_at']