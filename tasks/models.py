from django.db import models
from users.models import CustomUser

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    due_date = models.DateField()
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('C', 'Complete'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    document = models.FileField(upload_to='task_documents', blank=True, null=True)
    

    def __str__(self):
        return self.name
    

class Assignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='assignments')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assigned_on = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assigned_to.username} - {self.task.name}"
