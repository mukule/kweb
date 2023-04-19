from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import UserChangeForm




class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        label='',
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        label='',
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Enter First Name', 'class': 'form-control'}),
        label='',
       
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'class': 'form-control'}),
        label='',
        
    )
 

    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'autocomplete': 'new-password'}),
        
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control', 'autocomplete': 'new-password'}),
        
    )


    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

    
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'placeholder':'Staff Number', 'class':'form-control'})
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    


    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    job_function = forms.CharField(max_length=100, required=False)
    location = forms.CharField(max_length=100, required=False)
    phone = forms.CharField(max_length=100, required=False)
    contact_manager = forms.CharField(max_length=100, required=False)
    mood = forms.CharField(max_length=600, required=False)
    linkedin = forms.CharField(max_length=100, required=False)
    facebook = forms.CharField(max_length=100, required=False)
    twitter = forms.CharField(max_length=100, required=False)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'image', 'email', 'job_function', 'location', 'phone', 'contact_manager', 'mood', 'linkedin', 'facebook', 'twitter']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

class CustomUserChangeForm(UserChangeForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=False,
    )

    class Meta:
        model = get_user_model()
        fields = '__all__'


    