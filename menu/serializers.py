from rest_framework import serializers
from .models import Category, MenuItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'is_active']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'category', 'name', 'description', 'price', 'image', 'is_available', 'prep_time', 'created_at', 'updated_at' ]
        read_only_fields = ['created_at', 'updated_at']
