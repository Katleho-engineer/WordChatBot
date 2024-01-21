from rest_framework import serializers
from .models import Chat


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = "__all__"
        extra_kwargs = {'user_input': {'required': True}}