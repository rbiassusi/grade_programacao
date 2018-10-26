# coding: utf-8
from django.contrib import admin
from ..models import Radio


class RadioAdmin(admin.ModelAdmin):
    ordering = ('nome',)

    list_display = ('nome',)

    search_fields = ['nome']

admin.site.register(Radio, RadioAdmin)
