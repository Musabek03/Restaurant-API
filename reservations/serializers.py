from rest_framework import serializers
from .models import Reservation
from rest_framework.serializers import ValidationError



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'customer', 'table', 'date', 'time', 
                'guest_count', 'status', 'comment', 'created_at']
        read_only_fields = ['created_at']
    
    def validate(self, attrs):
        table = attrs.get('table')
        guest_count = attrs.get('guest_count')
        date = attrs.get('date')
        time = attrs.get('time')


        if table and guest_count:
            if guest_count > table.capacity:
                raise ValidationError({
                    "error": f"Keshirersiz, bul stolga kobi menen {table.capacity} adam siyatuginligi ushin {guest_count} orin bron qila almaysiz"
                })
        
        if table and date and time:
            existing_reservation = Reservation.objects.filter(table=table, date=date, time=time).exclude(status='cancelled')

            if existing_reservation.exists():
                raise ValidationError({
                    "error": "Bul stol korsetilgen waqit ham sanede bron etilgen. Basqa waqit yaki stol tanlan"
                })
            
        return attrs