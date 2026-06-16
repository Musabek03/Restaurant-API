from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import viewsets
from .permissions import IsOwnerReadOnly
from rest_framework import permissions


class ReviewViewSet(viewsets.ModelViewSet):
    
    model = Review.objects.all()
    serializer_class = ReviewSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsOwnerReadOnly]

    def perform_create(self, serializer):
        
        serializer.save(customer=self.request.user)
