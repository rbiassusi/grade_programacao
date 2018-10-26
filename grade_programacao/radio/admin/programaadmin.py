# coding: utf-8
from django.contrib import admin
from ..models import Programa, Programacao


class ProgramacaoInline(admin.TabularInline):
    model = Programacao


class ProgramaAdmin(admin.ModelAdmin):
    ordering = ('nome',)

    list_display = ('radio', 'nome', 'categoria',)
    list_filter = ('radio', 'categoria',)

    search_fields = ['nome', 'radio']

    inlines = [
        ProgramacaoInline,
    ]

admin.site.register(Programa, ProgramaAdmin)
