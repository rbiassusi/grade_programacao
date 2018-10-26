# -*- coding: utf-8 -*-
from django import forms
from ..models import Programacao


class ProgramacaoForm(forms.ModelForm):

    class Meta:
        model = Programacao
        fields = (
            'programa', 'data_inicio', 'data_fim'
        )

    def clean(self):
        cleaned_data = super(ProgramacaoForm, self).clean()

        if cleaned_data.get('data_inicio') > cleaned_data.get('data_fim'):
            self.add_error(
                'data_inicio', "Data de inicio não pode ser superior a data de fim")

        return cleaned_data
