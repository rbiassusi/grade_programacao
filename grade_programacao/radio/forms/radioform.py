# -*- coding: utf-8 -*-
from django import forms
from ..models import Radio


class RadioForm(forms.ModelForm):

    class Meta:
        model = Radio
        fields = (
            'nome',
        )
