from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


from .views import Chatting, Register, Logout, DeleteAccount

urlpatterns = [
    path('chat', Chatting.as_view(), name="chat-api"),
    path('login', obtain_auth_token, name="login-api"),
    path('register', Register.as_view(), name="register-api"),
    path('logout', Logout.as_view(), name="logout-api"),
    path('delete-account', DeleteAccount.as_view(), name="delete_account-api"),
]
