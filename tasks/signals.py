from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from notifications.models import Notification
from .models import Assignment

User = get_user_model()

@receiver(post_save, sender=Assignment)
def notify_assigned_user(sender, instance, created, **kwargs):
    if created and not instance.completed and isinstance(instance.assigned_to, User):
        message = f"You have been assigned a new task: {instance.task.name}"
        Notification.objects.create(user=instance.assigned_to, message=message, task_id=instance.task.id)
