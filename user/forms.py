from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm

from .validators import domain_validator

class CustomUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
        )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            "email",
        )
