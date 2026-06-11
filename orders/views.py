from django.shortcuts import render
from .models import Order, OrderItem, STATUS_CHOICES
from menu.models import MenuItem 
from .serializers import OrderSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from django.db.models import Sum



@extend_schema(tags=['Orders'])
class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    @action(detail=True, methods=['patch'])
    def status(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get('status')

        if not new_status:
            return Response({'error': "Status maydani jiberilmegen"}, status=status.HTTP_400_BAD_REQUEST)
        
        valid_statuses = [choice[0] for choice in STATUS_CHOICES]
        if new_status not in valid_statuses:
            return Response({'error': f"Naduris status! Ruxsat etilgen statuslar: {valid_statuses}"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        if order.status in ['cancelled', 'served']:
            if new_status == 'new':
                return Response({'error': "Biykarlangan yaki jetkerilgen buyirtpani qaytadan 'new' statusina ozgertiwge bolmaydi!"},
                                status=status.HTTP_400_BAD_REQUEST)
            
        order.status = new_status
        order.save()

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    @action(detail=True, methods=['post'], url_path='add-item')
    def add_item(self,  request, pk=None):
        order = self.get_object()

        if order.status in ['cancelled', 'served']:
            return Response({'error': "Biykarlangan yaki jabilgan buyirtpalarga jana tagam qosiwga bolmaydi "},
                            status=status.HTTP_400_BAD_REQUEST)
        
        menu_item_id = request.data.get('menu_item')
        quantity = request.data.get('quantity',1) 

        if not menu_item_id:
            return Response({"error": "menu_item kiritiliw shart!"})
        
        try:
            quantity = int(quantity)
            if quantity < 0:
                raise ValueError
        except ValueError:
                return Response({"error": "Quantity (sanı) nolden úlken pútin san bolıwı kerek!"},
                                 status=status.HTTP_400_BAD_REQUEST)
        
        menu_item = get_object_or_404(MenuItem, id=menu_item_id)

        order_item, created = OrderItem.objects.get_or_create(
            order=order,
            menu_item=menu_item,
            defaults={
                'quantity': quantity,
                'price': menu_item.price,
                'subtotal': menu_item.price * quantity
            }
        )

        if not created:
            order_item.quantity += quantity
            order_item.subtotal +=  order_item.price * order_item.quantity
            order_item.save()
        
        self.update_order_total(order)

        return Response({
            "message": "Taǵam buyırtpaǵa qosıldı.",
            "order_item_id": order_item.id,
            "quantity": order_item.quantity,
            "subtotal": order_item.subtotal
        }, status=status.HTTP_201_CREATED)

    
    @action(detail=True, methods=['post'], url_path='remove-item')
    def remove_item(self, request, pk=None):
        order = self.get_object()

        if order.status in ['cancelled', 'served']:
            return Response({'error': 'Jabilgan yamasa biykarlangan buyirtpani ozgertiwge bolmaydi!'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        order_item_id = request.data.get('order_item_id')
        
        if not order_item_id:
            return Response({'error': " 'order_item_id' kiritiliwi shart!"}, status=status.HTTP_400_BAD_REQUEST)
        
        order_item = get_object_or_404(OrderItem, id=order_item_id, order=order)
        order_item.delete()

        self.update_order_total(order)

        return Response({'message': 'Tagam buyiyrtpadan alip taslandi'})

    def update_order_total(self,order):

        total = order.orderitems.aggregate(total_sum=Sum('subtotal'))['total_sum']
        order.total_amount = total or 0.00 
        order.save()