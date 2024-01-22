from django.contrib import admin

from .models import Chat


class ChatAdmin(admin.ModelAdmin):
    readonly_fields = ("bot_response", "created")


admin.site.register(Chat, ChatAdmin)
