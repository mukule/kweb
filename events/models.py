from django.db import models
from users.models import CustomUser
import uuid
from django.utils import timezone
from tinymce.models import HTMLField






class Event(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    description = HTMLField(blank=True, default='')
    created_by = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    date_created = models.DateField(null=True, blank=True, auto_now_add=True)
    event_date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    is_main_event = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def has_already_occurred(self):
        """
        Returns True if the event has already occurred, False otherwise.
        """
        return self.event_date < timezone.now()

    def save(self, *args, **kwargs):
        if not self.id:
            # if the event is being created and the created_by field is not set,
            # set the created_by field to the current user
            if self.created_by is None:
                self.created_by = kwargs.pop('user', None)
        super(Event, self).save(*args, **kwargs)

        