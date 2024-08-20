from .base_model import BaseModel
from django.db import models


class User(BaseModel):
    full_name = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    class Meta:
        db_table = 'users'
