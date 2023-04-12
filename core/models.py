from django.db import models
from users.models import CustomUser


class Department(models.Model):
    name = models.CharField(max_length=100)
    hod = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='hod_department')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def staff_count(self):
        return self.staff.count()
    
class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    departments = models.ManyToManyField(Department, related_name='staff')
    telephone = models.CharField(max_length=20, default='')
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)
    start_date = models.DateField(blank=True, null=True, default=None)
    last_performance_review = models.DateField(blank=True, null=True, default=None)
    certifications = models.TextField(blank=True, default='')
    skills = models.TextField(blank=True, default='')
    

    def __str__(self):
        return self.user.username
