from django import forms
from .models import Task


class TaskUpdateForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('C', 'Complete'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}),
                               label='')

    class Meta:
        model = Task
        fields = ['status']
