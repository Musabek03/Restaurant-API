from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from drf_spectacular.utils import extend_schema



@extend_schema(tags=['Auth'])
class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]



@extend_schema(tags=['Users'])
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    