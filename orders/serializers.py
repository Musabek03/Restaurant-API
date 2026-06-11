from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'menu_item', 'quantity', 'price', 'subtotal']
        read_only_fields = ['price', 'subtotal']


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(source ='orderitems', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'items', 'customer', 'table', 'reservation', 'status', 'total_amount', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']



