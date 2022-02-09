from django.db import models
from django.contrib.auth.models import User, AbstractUser

from  accounts.managers import UserManager

# Create your models here.
GENDER_CHOICES = (
    ('male', 'Male'),
    ('female','Female')
)

class User(AbstractUser):
    """docstring for User."""
    username = None
    role = models.CharField(max_length=12, error_messages={'required':"Role must be provided"})
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False, error_messages={'unique':"A user with that email alrady exists.",
    })
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects  = UserManager()
