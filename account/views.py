from .models import CustomUser
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]