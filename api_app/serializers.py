from rest_framework import serializers
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from .models import Chat


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = "__all__"
        # fields = ['user_input']
        extra_kwargs = {'user_input': {'required': True}}


class ChatSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Chat
        # fields = "__all__"
        fields = ['user_input']
        extra_kwargs = {'user_input': {'required': True}}


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password2': {'write_only': True},
        }

    def save(self, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'P1 and P2 should be the same.'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exist.'})

        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error': 'Username already exist.'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account


# class RegisterResponseSerializer(serializers)