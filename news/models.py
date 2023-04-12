from django.db import models
from users.models import CustomUser
from django.utils import timezone
from django.urls import reverse
from intranet import settings
from tinymce.models import HTMLField


class News(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField(blank=True, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/', blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
    
