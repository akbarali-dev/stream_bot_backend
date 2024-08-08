from base_model import BaseModel
from django.db import models


class SportsType(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'sport_types'
