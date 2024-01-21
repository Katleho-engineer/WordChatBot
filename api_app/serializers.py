from rest_framework import serializers
from .models import Chat


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = "__all__"
        # extra_kwargs = {
        #     'host': {'read_only': True},
        # }