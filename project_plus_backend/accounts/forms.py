from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    """Class defines sign up form"""
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    full_name = forms.CharField(max_length=255, help_text='Required. Enter your full name.')

    class Meta:
        """The meta class"""
        model = User
        fields = ('email', 'full_name', 'password')

def save(self, commit=True):
    """The save function"""
    user = super(SignUpForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
        user.save()
    return user
