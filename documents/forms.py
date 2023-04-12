from django import forms
from .models import StaffDocument

class StaffDocumentForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    file = forms.FileField(
        label='File',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = StaffDocument
        fields = ['title', 'description', 'file']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.instance.user = user
