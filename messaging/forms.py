from django import forms
from .models import Message
from users.models import CustomUser



class MessageForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': 'form-control'}))
    body = forms.CharField(
    widget=forms.TextInput(attrs={'placeholder': 'Type your message here...', 'class': 'form-control'}),
    label='',
)


    class Meta:
        model = Message
        fields = ('recipient', 'body')

    def __init__(self, *args, **kwargs):
        self.sender = kwargs.pop('sender')
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['recipient'].queryset = CustomUser.objects.exclude(pk=self.sender.pk)
        self.fields['recipient'].label = 'Select a user to receive message'
    
    def save(self, commit=True):
        instance = super(MessageForm, self).save(commit=False)
        instance.sender = self.sender
        if commit:
            instance.save()
        return instance




class ReplyForm(MessageForm):
    reply_to = forms.IntegerField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        reply_to = kwargs.pop('reply_to')
        super().__init__(*args, **kwargs)
        self.fields['recipient'].widget = forms.HiddenInput()
        self.fields['reply_to'].initial = reply_to

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.sender = self.sender
        instance.parent_msg = Message.objects.get(pk=self.cleaned_data['reply_to'])
        if commit:
            instance.save()
        return instance
