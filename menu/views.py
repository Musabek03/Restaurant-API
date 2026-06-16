from rest_framework import viewsets, filters
from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer
from drf_spectacular.utils import extend_schema
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


@extend_schema(tags=['Categories'])
class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer



@extend_schema(tags=['Menu-Items'])
class MenuItemViewSet(viewsets.ModelViewSet):

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter ,DjangoFilterBackend]
    filterset_fields = ['category', 'is_available']
    ordering_fields = ["price", "name",]
    ordering = ["-price"]
    search_fields = ['name', 'description']