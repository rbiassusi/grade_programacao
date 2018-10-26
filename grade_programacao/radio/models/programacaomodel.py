# coding: utf-8
from django.db import models


class Programacao(models.Model):
    programa = models.ForeignKey('Programa', related_name='horarios')
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
