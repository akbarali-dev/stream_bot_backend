from django.dispatch import receiver
from environs import Env
import requests
from .base_model import BaseModel, PathAndRename
from django.db import models
from django.db.models.signals import pre_save
from django.contrib import messages
from django.core.exceptions import ValidationError

path_and_rename = PathAndRename("bot/sport_type/images/")


class SportsType(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=path_and_rename)
    file_id = models.CharField(max_length=255, blank=True, null=True,
                               help_text="To'ldirilishi shart emas!!! Server tomonidan amalga oshiriladi")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sport_types'


# @receiver(pre_save, sender=SportsType)
# def save_file_id(sender, instance, **kwargs):
#     print(instance.image)
#     instance.file_id = get_file_id(instance.image.url)


# def get_file_id(url):
#     env = Env()
#     env.read_env()
#     bot_token = env.str("BOT_TOKEN")
#     chat_id = '1474104201'
#
#     nn = "/home/akbarali/programming/python/personalProject/stream_bot_backend/media/"
#     image_path = nn + url
#     print(url)
#     print(image_path)
#     url = f'https://api.telegram.org/bot{bot_token}/sendPhoto1'
#     try:
#         with open(image_path, 'rb') as image_file:
#             files = {'photo': image_file}
#             data = {'chat_id': chat_id}
#             response = requests.post(url, data=data, files=files)
#         if response.status_code == 200:
#             response_data = response.json()
#             if response_data['ok']:
#                 file_id = response_data['result']['photo'][-1]['file_id']
#                 m_id = response_data['result']['message_id']
#                 d_url = f'https://api.telegram.org/bot{bot_token}/deleteMessage'
#                 data2 = {'chat_id': chat_id, 'message_id': m_id}
#                 response = requests.get(d_url, data=data2)
#                 return file_id
#             else:
#                 raise ValidationError(response_data)
#         else:
#             raise ValidationError(f'HTTP so‘rovda xatolik: {response.text}')
#     except Exception as e:
#         raise ValidationError(f'Xatolik yuz berdi: {str(e)}')
