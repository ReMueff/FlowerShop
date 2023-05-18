from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class User(AbstractUser):
    objects = UserManager()
    username = None
    email = models.EmailField(max_length=100, unique=True, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    first_name = None
    last_name = None

    def __str__(self):
        return self.email
