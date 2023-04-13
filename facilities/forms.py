from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    purpose = forms.CharField(
        label='Purpose',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    start_time = forms.DateTimeField(
        label='Start Time',
        widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker'})
    )
    end_time = forms.DateTimeField(
        label='End Time',
        widget=forms.DateTimeInput(attrs={'class': 'form-control datetimepicker'})
    )

    class Meta:
        model = Booking
        fields = ['purpose', 'start_time', 'end_time']
        
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError('The end time must be after the start time.')
