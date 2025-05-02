from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ShirtSerializer
from .models import Shirt
from rest_framework.permissions import IsAuthenticated, AllowAny

class ShirtListCreate(generics.ListCreateAPIView):
    serializer_class = ShirtSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can view their shirts
    
    def get_queryset(self):
        return Shirt.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(creator=self.request.user)  # Save the shirt with the current user
        else:
            print(serializer.errors)

class ShirtListDelete(generics.DestroyAPIView):
    serializer_class = ShirtSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete their shirts

    def get_queryset(self):
        user = self.request.user
        return Shirt.objects.filter(creator=user)
    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow any user to create an account
 