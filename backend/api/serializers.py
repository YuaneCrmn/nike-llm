from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Shirt

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class ShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shirt
        fields = ['id', 'title', 'description', 'usert', 'size', 'color', 'created_at']
        extra_kwargs = {
            'usert': {'read_only': True},
            'created_at': {'read_only': True}
        }