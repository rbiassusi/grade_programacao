# coding: utf-8
from django.db import models


class Radio(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome
