from django.contrib import admin
from ..models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    ordering = ('nome',)

    list_display = ('nome', 'ordem_prioridade',)

    search_fields = ['nome']

admin.site.register(Categoria, CategoriaAdmin)