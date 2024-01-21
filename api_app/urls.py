from django.urls import path

from .views import Chatting

urlpatterns = [
    path('chat', Chatting.as_view(), name="chat-api"),
]
