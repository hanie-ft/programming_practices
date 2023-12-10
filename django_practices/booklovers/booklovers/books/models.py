from django.db import models
from booklovers.common.models import BaseModel

# Create your models here.


class Book(BaseModel):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=150, blank=True, null=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return {self.title, self.author, self.publisher, self.category}
