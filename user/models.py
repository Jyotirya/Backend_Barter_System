from django.db import models
from django.urls import reverse
from .validators import domain_validator
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    email = models.EmailField(unique=True, validators=[domain_validator])
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
