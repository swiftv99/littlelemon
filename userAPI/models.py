from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    # username = models.CharField(max_length=255, unique=True)
    # email = models.EmailField(unique=True)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), unique=True, error_messages={
            "unique": _("A user with that email already exists.")})
    
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('company', 'Company'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        ordering = ['email']

    def str(self):
        return self.email
