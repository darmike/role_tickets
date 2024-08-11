from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Модель користувача
class User(AbstractUser):
    role = models.CharField(max_length=50)

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
