from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "password", "is_staff", "is_admin")


class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "password")



class EmployeeLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["email"], password=data["password"])
        if user and not user.is_staff:
            return user
        raise serializers.ValidationError("Invalid credentials or not an employee.")
