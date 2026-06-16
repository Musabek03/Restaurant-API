from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.Serializer):
    
    class Meta:
        model = Review
        fields = ['customer', 'rating', 'comment', 'created_at']
        

