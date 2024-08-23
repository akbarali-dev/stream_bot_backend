import os
import requests
from environs import Env

from django import forms
from django.utils.html import mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from .base_model import BaseModel, PathAndRename
from .sport_type import SportsType
from .channel import Channel
from ckeditor.fields import RichTextField

# from celery import shared_task

path_and_rename = PathAndRename("bot/competition/images/")


class Competition(BaseModel):
    name = models.CharField(max_length=255)
    description = RichTextField()
    channels = models.ManyToManyField(Channel, blank=True, null=True)
    start_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    sport_type = models.ForeignKey(SportsType, on_delete=models.CASCADE, related_name='competitions')
    image = models.ImageField(upload_to=path_and_rename)
    file_id = models.CharField(max_length=255, blank=True, null=True,
                               help_text="Bu maydon to'dirilishi shart emas server tomondan qo'ldiriladi")
    stream_link = models.URLField(max_length=255, null=True, blank=True,
                                  help_text="Steam boshlanganda havolani qo'shing")
    send_bot = models.BooleanField(default=False)
    send_channel = models.BooleanField(default=False)

    _temp_field = None

    def set_temp_field(self, value):
        self._temp_field = value

    def get_temp_field(self):
        return self._temp_field

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    # Bu maydon admin panelda ishlatiladi, lekin ma'lumotlar bazasiga saqlanmaydi
    temp_field = property(get_temp_field, set_temp_field)

    def img_preview(self):
        return mark_safe('<img src = "{url}" width = "100"/>'.format(
            url=self.image.url
        ))

    img_preview.short_description = 'Image'

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'competition'

# @shared_task
# def process_image(image_url):
#     # Logic to notify aiogram server about the new image
#     print(f"Processing image: {image_url}")


# @receiver(post_save, sender=Competition)
# def my_model_post_save(sender, instance, **kwargs):
#     env = Env()
#     env.read_env()
#     bot_token = env.str("BOT_TOKEN")
#     chat_id = '1474104201'
#
#     nn = "/home/akbarali/programming/python/personalProject/stream_bot_backend"
#     image_path = nn+instance.image.url
#     url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
#
#     with open(image_path, 'rb') as image_file:
#         files = {'photo': image_file}
#         data = {'chat_id': chat_id}
#         response = requests.post(url, data=data, files=files)
#
#     if response.status_code == 200:
#         response_data = response.json()
#         if response_data['ok']:
#             file_id = response_data['result']['file_id']
#             print('Rasm muvaffaqiyatli yuborildi!')
#             print(f'File ID: {file_id}')
#             return file_id
#         else:
#             print('Telegram API xatolik qaytardi:', response_data)
#     else:
#         print('Xatolik yuz berdi:', response.text)
#
#     print(f"Signal: {instance.name} saqlandi!")
