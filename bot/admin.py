from bs4 import BeautifulSoup

from .models import *
from django.contrib import admin
from django.utils.html import format_html
from environs import Env
from django.contrib import messages
import requests
from copy import deepcopy
from config.settings import DEBUG

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'active')
    search_fields = ('full_name',)


@admin.register(SportsType)
class SportsTypeAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ('name', 'image_tag')
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # if obj.image and not obj.file_id:
        obj.file_id = get_file_id(request, obj.image.url)
        obj.save(update_fields=['file_id'])


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ('name', 'start_date', 'active', 'image_tag')
    search_fields = ('name',)
    readonly_fields = ['img_preview', ]

    def update_model(self, request, obj, form, change):
        obj.description = self.remove_tags(obj.description)

        super().save_model(request, obj, form, change)

    def save_model(self, request, obj, form, change):
        old_image = deepcopy(obj.image)
        obj.description = self.remove_tags(obj.description)
        super().save_model(request, obj, form, change)
        if old_image != obj.image:
            obj.file_id = get_file_id(request, obj.image.url)
            obj.save(update_fields=['file_id'])
            # env = Env()
            # env.read_env()
            # bot_token = env.str("BOT_TOKEN")
            # chat_id = '1474104201'
            #
            # nn = "/home/akbarali/programming/python/personalProject/stream_bot_backend"
            # image_path = nn + obj.image.url
            # url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
            #
            # # try:
            # with open(image_path, 'rb') as image_file:
            #     files = {'photo': image_file}
            #     data = {'chat_id': chat_id}
            #     response = requests.post(url, data=data, files=files)
            #
            # if response.status_code == 200:
            #     response_data = response.json()
            #     print(response_data)
            #     if response_data['ok']:
            #         file_id = response_data['result']['photo'][-1]['file_id']
            #         m_id = response_data['result']['message_id']
            #         obj.file_id = file_id
            #         obj.save(update_fields=['file_id'])
            #         messages.success(request, f'Rasm muvaffaqiyatli yuborildi! File ID: {file_id}')
            #         d_url = f'https://api.telegram.org/bot{bot_token}/deleteMessage'
            #         data2 = {'chat_id': chat_id, 'message_id': m_id}
            #         response = requests.get(d_url, data=data2)
            #     else:
            #         messages.error(request, f'Telegram API xatolik qaytardi: {response_data}')
            # else:
            #     messages.error(request, f'HTTP so‘rovda xatolik: {response.text}')
        # except Exception as e:
        #     messages.error(request, f'Xatolik yuz berdi: {str(e)}')

    def remove_tags(self, text):
        soup = BeautifulSoup(text, "html.parser")
        for p in soup.find_all('p'):
            p.unwrap()  # <p> tegini olib tashlaydi, lekin ichidagi matnni saqlaydi
        return str(soup)


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'username',)
    search_fields = ('name', 'username',)


def get_file_id(request, url):
    env = Env()
    env.read_env()
    bot_token = env.str("BOT_TOKEN")
    chat_id = '1474104201'
    if DEBUG:
        nn = "/home/akbarali/programming/python/personalProject/stream_bot_backend"
    else:
        nn = "/root/stream_bot_backend"
    image_path = nn + url
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    try:
        with open(image_path, 'rb') as image_file:
            files = {'photo': image_file}
            data = {'chat_id': chat_id}
            response = requests.post(url, data=data, files=files)
        if response.status_code == 200:
            response_data = response.json()
            if response_data['ok']:
                file_id = response_data['result']['photo'][-1]['file_id']
                m_id = response_data['result']['message_id']
                messages.success(request, f'Rasm muvaffaqiyatli yuborildi! File ID: {file_id}')
                d_url = f'https://api.telegram.org/bot{bot_token}/deleteMessage'
                data2 = {'chat_id': chat_id, 'message_id': m_id}
                response = requests.get(d_url, data=data2)
                return file_id
            else:
                messages.error(request, f'Telegram API xatolik qaytardi: {response_data}')
        else:
            messages.error(request, f'HTTP so‘rovda xatolik: {response.text}')
    except Exception as e:
        messages.error(request, f'Xatolik yuz berdi: {str(e)}')
