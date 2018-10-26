from django.contrib import admin
from ..models import Programacao


class ProgramacaoAdmin(admin.ModelAdmin):
    ordering = ('programa',)

    list_display = ('programa', 'data_inicio', 'data_fim',)
    

    search_fields = ['programa']

admin.site.register(Programacao, ProgramacaoAdmin)