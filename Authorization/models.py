from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class User(AbstractUser, BaseModel):
    email = models.EmailField(
        'email address',
        max_length=150, 
        unique=True, 
        blank=False,
        help_text = "Required. Enter a valid email address",
        error_messages={
            'unique': "A user with that email already exists.",
        })
    username = models.CharField(
        max_length=150,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': ("A user with that username already exists."),
        },
        blank=True
    )
    name = models.CharField(
        max_length=150,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': ("A user with that name already exists."),
        },
        blank=True
    )
    bio = models.TextField(max_length=255, default='all about me')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
