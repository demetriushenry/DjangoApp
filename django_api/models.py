from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone

from .managers import UserManager


# Create your models here.
class User(AbstractUser):

    username_validator = UnicodeUsernameValidator()

    username = None
    name = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': "A user with that name already exists.",
        },
    )
    birthday = models.DateField(default=timezone.now)
    cpf = models.CharField(max_length=11, unique=True)
    cep = models.CharField(max_length=9)
    street = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.name
