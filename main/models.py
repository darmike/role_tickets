from django.contrib.auth.models import AbstractUser, Group as DefaultGroup, Permission
from django.db import models


# Модель користувача
class User(AbstractUser):
    role = models.CharField(max_length=50)
    groups = models.ManyToManyField(
        DefaultGroup,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user',
    )


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
