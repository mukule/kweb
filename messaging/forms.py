from django import forms
from .models import Message
from users.models import CustomUser


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('recipient', 'body', 'attachment', 'image')

    def __init__(self, *args, **kwargs):
        self.sender = kwargs.pop('sender')
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['recipient'].queryset = CustomUser.objects.exclude(pk=self.sender.pk)

    def save(self, commit=True):
        instance = super(MessageForm, self).save(commit=False)
        instance.sender = self.sender
        if commit:
            instance.save()
        return instance
