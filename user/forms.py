from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .validators import domain_validator

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            'password',
        )

class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
        )