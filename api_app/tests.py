from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework.authtoken.models import Token

from django.urls import reverse
from django.contrib.auth.models import User


class TestChat(APITestCase):

    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=user)

    def test_chat_post(self):
        data = {
            "host": "1",
            'user_input': "empty",
            "bot_response": "Please type something so that we can chat :("
        }
        url = reverse('chat-api')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_chat_get(self):
        url = reverse('chat-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_chat_delete(self):
        url = reverse('chat-api')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            'username': 'test',
            'email': 'test@gmail.com',
            'password': 'Password@123',
            'password2': 'Password@123',
        }

        url = reverse('register-api')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginLogoutTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='one@gmail.com', password='Password@123', email='one@gmail.com')

    def test_login(self):
        data = {
            'username': 'one@gmail.com',
            'password': 'Password@123',
            'email': 'one@gmail.com',
        }

        url = reverse('login-api')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username='one@gmail.com')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        url = reverse('logout-api')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
