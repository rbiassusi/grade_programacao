# coding: utf-8
from django.db import models


class Programa(models.Model):
    radio = models.ForeignKey('Radio')
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey('Categoria')

    def __str__(self):
        return self.nome
