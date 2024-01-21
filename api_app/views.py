from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Chat
from .serializers import ChatSerializer

from Bot.main import get_response

from django.http import JsonResponse


class Chatting(APIView):

    def get(self, request):
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request):

        user_input = request.data['user_input']

        # Check if input is empty
        if user_input == "":
            data = {
                'user_input': "empty",
                "bot_response": "Please type something so that we can chat :("
            }

        else:
            bot_response = get_response(user_input)

            data = {
                'user_input': user_input,
                "bot_response": f"{bot_response}"
            }

        serializer = ChatSerializer(data=data)

        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data['bot_response'])

        else:
            return Response(serializer.errors)

    def delete(self, request):
        chats = Chat.objects.all()
        chats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
