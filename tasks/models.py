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
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    document = models.FileField(upload_to='task_documents', blank=True, null=True)
    

    def __str__(self):
        return self.name
    

class Assignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='assignments')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assigned_on = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    additional_details = models.TextField(blank=True)
    rejection_reason = models.TextField(blank=True)
   
    def __str__(self):
        return f"{self.assigned_to.username} - {self.task.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.accepted:
            self.task.status = 'I'
            self.task.save()
        elif self.task.assignments.filter(accepted=True).count() == 0:
            self.task.status = 'P'
            self.task.save()

    def mark_complete(self):
        self.task.status = 'C'
        self.task.save()



class ProgressReport(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='progress_reports')
    report = models.TextField()
    report_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='progress_reports/', blank=True)

    def __str__(self):
        return f"Progress Report for {self.assignment.task.name} by {self.assignment.assigned_to.username}"
