from django.db import models
from users.models import CustomUser
from django.urls import reverse
from tasks.models import Task

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, default='')
    message = models.CharField(max_length=200)
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('task_detail', args=(self.task.pk))


