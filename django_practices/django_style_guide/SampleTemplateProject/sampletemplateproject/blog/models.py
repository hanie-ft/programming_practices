from django.db import models

from sampletemplateproject.common.models import BaseModel

# Create your models here.

class Product(BaseModel):
    name = models.TextField(max_length=255)
