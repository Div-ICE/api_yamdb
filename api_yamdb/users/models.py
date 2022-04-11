from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils import Choices


class User(AbstractUser):
    ROLE = Choices(
        ('U', 'user'),
        ('M', 'moderator'),
        ('A', 'admin'),
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        max_length=1,
        choices=ROLE,
        default=ROLE.U)


"""
Сделано по этому образцу. оставил для доработки serializers и viewsets

тред
https://stackoverflow.com/questions/28945327/django-rest-framework-with-choicefield
источник ответа
https://stackoverflow.com/a/34775194/17683875


# models.py
from model_utils import Choices

class User(AbstractUser):
    GENDER = Choices(
       ('M', 'Male'),
       ('F', 'Female'),
    )

    gender = models.CharField(max_length=1, choices=GENDER, default=GENDER.M)


# serializers.py 
from rest_framework import serializers

class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)

class UserSerializer(serializers.ModelSerializer):
    gender = ChoicesField(choices=User.GENDER)

    class Meta:
        model = User

# viewsets.py
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""