from base_model import BaseModel
from django.db import models


class User(BaseModel):
    full_name = models.CharField(max_length=255)
