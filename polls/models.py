from django.db import models
from users.models import CustomUser
from django.utils import timezone

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=7))

    def is_active(self):
        return self.pub_date <= timezone.now() <= self.end_date
    
    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    voters = models.ManyToManyField(CustomUser, blank=True)

    def __str__(self):
        return self.choice_text
