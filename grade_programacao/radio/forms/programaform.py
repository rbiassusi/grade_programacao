# -*- coding: utf-8 -*-
from django import forms
from ..models import Programa


class ProgramaForm(forms.ModelForm):

    class Meta:
        model = Programa
        fields = (
            'radio', 'nome', 'categoria'
        )
