from django.utils.html import mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver
from .base_model import BaseModel, PathAndRename
from django.db import models
from .sport_type import SportsType

path_and_rename = PathAndRename("bot/competition/images/")


class Competition(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    sport_type = models.ForeignKey(SportsType, on_delete=models.CASCADE, related_name='competitions')
    image = models.ImageField(upload_to=path_and_rename)
    stream_link = models.URLField(max_length=255, null=True, blank=True)

    def img_preview(self):
        return mark_safe('<img src = "{url}" width = "100"/>'.format(
            url=self.image.url
        ))

    img_preview.short_description = 'Image'

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'competition'


# @receiver(post_save, sender=Competition)
# def my_model_post_save(sender, instance, **kwargs):
#     print(f"Signal: {instance.name} saqlandi!")
