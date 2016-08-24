from django import forms
from registration.forms import RegistrationForm

from .models import User as CustomUser


class CustomUserRegistrationForm(RegistrationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'bio')
