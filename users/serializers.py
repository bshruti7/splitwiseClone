from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validate_data):
        validate_data["password"] = make_password(validate_data['password'])
        user = User.objects.create(**validate_data)
        # UserProfile.objects.create(user=user)
        return user


    class Meta:
        model = User
        fields = ('username', 'email', 'password')
