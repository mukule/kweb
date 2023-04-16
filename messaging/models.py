from django.db import models
from users.models import CustomUser

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'Message from {self.sender} to {self.recipient} sent on {self.timestamp}'

    def is_reply(self):
        return self.reply_to is not None

    def get_replies(self):
        return Message.objects.filter(reply_to=self).order_by('timestamp')
