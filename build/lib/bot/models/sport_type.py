from .base_model import BaseModel, PathAndRename
from django.db import models

path_and_rename = PathAndRename("bot/sport_type/images/")


class SportsType(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=path_and_rename)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sport_types'
