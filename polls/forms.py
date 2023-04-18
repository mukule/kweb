from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Choice

class VoteForm(forms.Form):
    choice = forms.ModelChoiceField(
        queryset=Choice.objects.all(),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        empty_label=None,
        error_messages={
            'required': _('You must select a choice to vote.'),
        }
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.poll = kwargs.pop('poll')
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = self.poll.choice_set.exclude(choice_text='')
        self.fields['choice'].label = _('Select your choice')

    def clean_choice(self):
        choice = self.cleaned_data['choice']
        if self.user in choice.voters.all():
            raise forms.ValidationError(_('You have already voted for this choice.'))
        return choice
