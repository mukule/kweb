from django import forms
from .models import Event
from tinymce.models import HTMLField


class EventForm(forms.ModelForm):
    name = forms.CharField(
        label='Event name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    event_date = forms.DateTimeField(
        label='Event date',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}, format='%Y-%m-%dT%H:%M')
    )

    location = forms.CharField(
        label='Location',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    image = forms.ImageField(
        label='Image',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Event
        fields = ['name', 'description', 'event_date', 'location', 'image']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
