from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Chat(models.Model):
    host = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='host_chat')
    user_input = models.CharField(max_length=200)
    bot_response = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.user_input}"
