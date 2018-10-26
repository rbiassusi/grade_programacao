# coding: utf-8
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    ordem_prioridade = models.IntegerField(
        default=0, help_text=u"0 - não tem prioridade, Quanto maior o número maior a prioridade")

    def __str__(self):
        return self.nome
