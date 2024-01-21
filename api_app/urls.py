from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


from .views import Chatting, Login

urlpatterns = [
    path('chat', Chatting.as_view(), name="chat-api"),
    path('login', obtain_auth_token, name="login-api"),
]
