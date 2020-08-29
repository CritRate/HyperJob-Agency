from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Vacancy(models.Model):
    description = models.TextField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)