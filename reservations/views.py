from rest_framework import viewsets
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Reservations'])
class ReservationViewSet(viewsets.ModelViewSet):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


    @action(detail=True, methods=['post'])
    def confirm(self,request, pk=None):
        reservation = self.get_object() # Bazadan soralgan (id=pk) brondi aladi

        if reservation.status == 'cancelled':
            return Response({
                "error": "Biykarlangan brondi tastiyqlaw mumkin emes!"
            }, status=status.HTTP_400_BAD_REQUEST)

        if reservation.status == 'confirmed':
            return Response({
                "error": "Bul bron alleqashan tastiyqlangan!"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        reservation.status =='confirmed'
        reservation.save()
        return Response({'message': "Bron tastiyqlandi"}, status=status.HTTP_200_OK)


    @action(detail=True, methods=['post'])
    def cancel(self,request, pk=None):
        reservation = self.get_object()

        if reservation.status == 'cancelled':
            return Response({
                'error': 'Bul bron alleqashan biykarlangan!'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        reservation.status = 'cancelled'
        reservation.save()
        return Response({'message': 'Bron biykarlandi'}, status=status.HTTP_200_OK)