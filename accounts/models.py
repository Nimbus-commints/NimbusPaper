from django.db import models
from django.contrib.auth.models import AbstractUser  # added

# Create your models here.


class CustomUser(AbstractUser):  # added
    age = models.PositiveIntegerField(null=True, blank=True)
    # null - database related
    # blank - validation related
