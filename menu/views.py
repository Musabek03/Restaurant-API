from rest_framework import viewsets
from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Categories'])
class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=['Menu-Items'])
class MenuItemViewSet(viewsets.ModelViewSet):

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer