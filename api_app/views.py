from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from rest_framework.authtoken.models import Token
from . import models

from .serializers import ChatSerializer, RegistrationSerializer, ChatSerializer2

from Bot.main import get_response

from django.contrib.auth.models import User

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

suggestions = """
    Use the following key words to get an accurate response:
        - Define
        - Antonym
        - Synonym
        - Syllables
        - Part of 
        - Pronunciation
        - Use in a sentence
        - everything 


    Here are the examples of request to make:
        ~ define ambient
        ~ Antonym of success
        ~ Synonym of life
        ~ Syllables of complicated
        ~ a wheel is part of
        ~ pronunciation of bombastic
        ~ Use careful in a sentence
        ~ Give me everything about lemon
     """


class Chatting(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    @swagger_auto_schema(operation_description='This will return all the chats between the user and chatbot.')
    def get(self, request):
        user = request.user.username
        host = User.objects.get(username=user)
        chats = host.host_chat.all()

        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ChatSerializer2, operation_description=suggestions)
    def post(self, request):
        user = request.user.username
        host = User.objects.get(username=user)

        user_input = request.data['user_input']

        # Checks if input is empty
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

    @swagger_auto_schema(operation_description='This will delete all the chats between the user and chatbot.')
    def delete(self, request):
        user = request.user.username
        host = User.objects.get(username=user)

        chats = host.host_chat.all()
        chats.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class Register(APIView):
    throttle_classes = [AnonRateThrottle]

    response = {
        "token": "b9756ccbe2ed8b7ef24754ba2e18befda6cb6799"
    }
    user_response = openapi.Response('response description', RegistrationSerializer)

    @swagger_auto_schema(request_body=RegistrationSerializer)
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


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description='This will logout the user.')
    def post(self, request):
        data = {
            "response": "Logged out successfully"
        }
        request.user.auth_token.delete()
        return Response(data, status=status.HTTP_200_OK)


class DeleteAccount(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="This will delete the user's account.")
    def delete(self, request):
        user = request.user
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
