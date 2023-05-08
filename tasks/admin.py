from django import forms
from django.contrib import admin
from .models import Task, Milestone
from django.db import models

class MilestoneInline(admin.TabularInline):
    model = Milestone
    extra = 1
    formfield_overrides = {
        models.DateField: {'widget': forms.DateInput(attrs={'type': 'date'})},
    }

class TaskAdmin(admin.ModelAdmin):
    inlines = [MilestoneInline]
    list_display = ['name', 'priority', 'due_date', 'status']

admin.site.register(Task, TaskAdmin)
