from rest_framework import viewsets
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework.decorators import action



class ReservationViewSet(viewsets.ModelViewSet):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


    @action(detail=True, methods=['post'])
    def confirm(self,request, pk=None):
        ...
    
    @action(detail=True, methods=['post'])
    def cancel(self,request, pk=None):
        ...