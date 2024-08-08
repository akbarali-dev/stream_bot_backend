from base_model import BaseModel
from django.db import models


class Competition(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    sport_type = models.ForeignKey('SportType', on_delete=models.CASCADE, related_name='competitions')
    image = models.ImageField(upload_to='competitions')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'competition'
