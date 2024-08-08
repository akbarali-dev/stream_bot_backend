from .models import *
from django.contrib import admin
from django.utils.html import format_html


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'blocked')
    search_fields = ('full_name',)


@admin.register(SportsType)
class SportsTypeAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ('name', 'image_tag')
    search_fields = ('name',)


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    list_display = ('name', 'start_date', 'active', 'image_tag')
    search_fields = ('name',)
    readonly_fields = ['img_preview', ]


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'username',)
    search_fields = ('name', 'username',)
