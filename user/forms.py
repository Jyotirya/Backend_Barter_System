from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .validators import domain_validator

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "first_name",
            "last_name",
            "address1",
            "address2",
            "is_active",
            "is_staff"]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            "address1",
            "address2"
        )