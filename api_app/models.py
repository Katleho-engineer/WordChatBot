from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    host = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='host_chat')
    user_input = models.CharField(max_length=200)
    bot_response = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.user_input}"
