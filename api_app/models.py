from django.db import models

# Create your models here.


class Chat(models.Model):
    user_input = models.CharField(max_length=200)
    bot_response = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.user_input}"
