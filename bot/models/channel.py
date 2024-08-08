from base_model import BaseModel
from django.db import models


class Channel(BaseModel):
    name = models.CharField(max_length=255)
    blocked = models.BooleanField(default=False)
    username = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'channels'
