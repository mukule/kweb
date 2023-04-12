from django.contrib import admin
from .models import Task, Assignment

# Register your models here.
admin.site.register(Task)
admin.site.register(Assignment)