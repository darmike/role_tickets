from django.contrib.auth.models import AbstractUser
from django.db import models

# Модель користувача
class User(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Адміністратор'),
        ('Manager', 'Менеджер'),
        ('Analyst', 'Аналітик'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    # Виключаємо стандартні ManyToMany поля
    groups = models.ManyToManyField('Group', related_name='users', blank=True)
    user_permissions = models.ManyToManyField('Permission', related_name='users', blank=True)


# Модель групи
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Модель прав доступу (Permission)
class Permission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Модель квитка
class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
