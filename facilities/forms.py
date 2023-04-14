from django import forms
from .models import Booking
from django.utils import timezone
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput


class BookingForm(forms.ModelForm):
    purpose = forms.CharField(
        label='Purpose',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
   
    date = forms.DateField(
        label='Date',
        widget=DatePickerInput(attrs={'class': 'form-control datepicker'}),
        initial=timezone.now().date(),
        input_formats=['%Y-%m-%d']
    )
    start_time = forms.DateTimeField(
        label='Start Time',
        widget=DateTimePickerInput(
            attrs={'class': 'form-control'},
            options={
                'format': 'HH:mm',
                'stepping': 15,
                'sideBySide': True,
                'icons': {
                    'time': 'fa fa-clock-o',
                    'date': 'fa fa-calendar',
                    'up': 'fa fa-chevron-up',
                    'down': 'fa fa-chevron-down',
                    'previous': 'fa fa-chevron-left',
                    'next': 'fa fa-chevron-right',
                    'today': 'fa fa-calendar-check-o',
                    'clear': 'fa fa-trash',
                    'close': 'fa fa-times'
                }
            }
        ),
        input_formats=['%Y-%m-%d %H:%M']
    )
    
    end_time = forms.DateTimeField(
        label='End Time',
        widget=DateTimePickerInput(
            attrs={'class': 'form-control'},
            options={
                'format': 'HH:mm',
                'stepping': 15,
                'sideBySide': True,
                'icons': {
                    'time': 'fa fa-clock-o',
                    'date': 'fa fa-calendar',
                    'up': 'fa fa-chevron-up',
                    'down': 'fa fa-chevron-down',
                    'previous': 'fa fa-chevron-left',
                    'next': 'fa fa-chevron-right',
                    'today': 'fa fa-calendar-check-o',
                    'clear': 'fa fa-trash',
                    'close': 'fa fa-times'
                }
            }
        ),
        input_formats=['%Y-%m-%d %H:%M']
    )
    class Meta:
        model = Booking
        fields = ['purpose', 'date', 'start_time', 'end_time']
        
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError('The end time must be after the start time.')
