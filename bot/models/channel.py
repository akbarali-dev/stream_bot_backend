from .base_model import BaseModel
from django.db import models


class Channel(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'channels'
