from django.db import models
from booklovers.common.models import BaseModel
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser, BaseModel):
    friends = models.ManyToManyField("CustomUser", blank=True)
    # profile_picture = models.ImageField(blank=True)
