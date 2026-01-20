from django.db import models
from .validators import domain_validator
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    email = models.EmailField(unique=True, validators=[domain_validator])
    username = None

    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)

    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()