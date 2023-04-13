from django.db import models
from users.models import CustomUser
from django.utils import timezone

class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()
    image = models.ImageField(upload_to='facilities/', default='facilities/images/default.jpg', blank=True, null=True)  # new field

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    purpose = models.TextField()
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.facility.name} booking by {self.user.username}'
