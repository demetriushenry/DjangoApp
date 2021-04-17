from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True)
    cep = models.CharField(max_length=9)
    street = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
