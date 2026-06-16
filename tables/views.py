from rest_framework import viewsets
from .models import Table 
from .serializers import TableSerializer
from drf_spectacular.utils import extend_schema
from .permissions import IsAdminOrReadOnly


@extend_schema(tags=['Tables'])
class TableViewSet(viewsets.ModelViewSet):

    queryset = Table.objects.all()
    serializer_class = TableSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAdminOrReadOnly]