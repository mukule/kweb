from django.contrib.auth.models import AbstractUser
from django.db import models
import os

class CustomUser(AbstractUser):

    STATUS = (
        ('Attachment', 'Attachment'),
        ('Intern', 'Intern'),
        ('Contract', 'Contract'),
        ('Permanent', 'Permanent'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    job_function = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    contact_manager = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    mood = models.CharField(max_length=600, default='', blank=True)

    def __str__(self):
        return self.username
    

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Users', self.username, instance)
        return None

    image = models.ImageField(default='default/user.png', upload_to=image_upload_to)

