from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from rest_framework.authtoken.models import Token
from . import models

from django.contrib.auth import login, authenticate

from .models import Chat
from .serializers import ChatSerializer, RegistrationSerializer

from Bot.main import get_response

from django.contrib.auth.models import User


class Chatting(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request):
        user = request.user.username
        host = User.objects.get(username=user)
        chats = host.host_chat.all()
        # chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request):

        user = request.user.username
        host = User.objects.get(username=user)

        user_input = request.data['user_input']

        # Check if input is empty
        if user_input == "":
            data = {
                "host": host.id,
                'user_input': "empty",
                "bot_response": "Please type something so that we can chat :("
            }

        else:
            bot_response = get_response(user_input)

            data = {
                "host": host.id,
                'user_input': user_input,
                "bot_response": f"{bot_response}"
            }

        serializer = ChatSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data['bot_response'], status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors)

    def delete(self, request):
        user = request.user.username
        host = User.objects.get(username=user)

        chats = host.host_chat.all()
        chats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Register(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key

            data['token'] = token

        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_201_CREATED)

