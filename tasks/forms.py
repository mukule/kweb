from django import forms
from .models import Task, Assignment, ProgressReport


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


class AssignmentAcceptForm(forms.Form):
    additional_details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    accept = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class ProgressReportForm(forms.ModelForm):
    class Meta:
        model = ProgressReport
        fields = ['report', 'file']
        widgets = {
            'report': forms.Textarea(attrs={'rows': 3}),
        }

        
class AssignmentRejectForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['rejection_reason']
        widgets = {
            'rejection_reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
