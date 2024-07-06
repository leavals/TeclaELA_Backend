from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from .models import Image
from .serializers import UserSerializer, ImageSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
