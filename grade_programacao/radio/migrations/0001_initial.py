# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-26 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('ordem_prioridade', models.IntegerField(default=0, help_text='0 - n\xe3o tem prioridade, Quanto maior o n\xfamero maior a prioridade')),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Programacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='radio.Programa')),
            ],
        ),
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='programa',
            name='radio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.Radio'),
        ),
    ]