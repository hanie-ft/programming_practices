from django.db import models
from django.contrib import admin

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

from booklovers.common.models import BaseModel


class CustomUserManager(BaseUserManager):
    def create_user(
        self, email, username, is_active=True, is_admin=False, password=None
    ):
        if not username:
            raise ValueError("The given username must be set")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            is_active=is_active,
            is_admin=is_admin,
        )
        user.set_password(password)
        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            username=username,
            email=email,
            is_active=True,
            is_admin=True,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, BaseModel, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    email = models.EmailField(verbose_name="email address", unique=True)
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
    # friends = models.ManyToManyField("CustomUser", blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email, self.username

    def is_staff(self):
        return self.is_admin

