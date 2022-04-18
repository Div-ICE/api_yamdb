from django.contrib.auth.models import AbstractUser
from django.db import models

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

class User(AbstractUser):
    ROLE = (
        (USER, USER),
        (MODERATOR, MODERATOR),
        (ADMIN, ADMIN),
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль пользователя',
        choices=ROLE,
        max_length=max(len(role[1]) for role in ROLE), default=USER
    )

    email = models.EmailField(
        'Электронная почта',
        unique=True,
        max_length=254,
    )

    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True
    )

    def is_admin(self):
        return (
            self.role == self.ROLE.A
            or self.is_staff
        )

    def is_moderator(self):
        return self.role == self.ROLE.M

    def __str__(self):
        return self.username
