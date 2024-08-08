from base_model import BaseModel
from django.db import models


class User(BaseModel):
    full_name = models.CharField(max_length=255)
    blocked = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'
