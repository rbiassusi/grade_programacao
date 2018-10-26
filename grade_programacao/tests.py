# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from radio.models import Radio, Programa, Categoria, Programacao
from django.utils import timezone
import json

RADIOS = [
    {"id": 1, "nome": "radio 1"},
    {"id": 2, "nome": "radio 2"},
    {"id": 3, "nome": "radio 3"}
]

CATEGORIAS = [
    {"id": 1, "nome": "categoria 1", "ordem_prioridade": 0},
    {"id": 2, "nome": "categoria 2", "ordem_prioridade": 50},
    {"id": 3, "nome": "categoria 3", "ordem_prioridade": 100}
]


PROGRAMAS = [
    {"id": 1, "nome": "programa 1", "radio_id": 1,"categoria_id": 1},
    {"id": 2, "nome": "programa 2", "radio_id": 2, "categoria_id": 2},
    {"id": 3, "nome": "programa 3", "radio_id": 3, "categoria_id": 3},
    {"id": 4, "nome": "programa 4", "radio_id": 1, "categoria_id": 2},
]

PROGRAMACAO = [
    [
        {
            "data_fim": "2018-10-22T20:00:00",
            "data_inicio": "2018-10-22T18:00:00",
            "programa_id": 1
        },
        {
            "data_fim": "2018-10-23T20:00:00",
            "data_inicio": "2018-10-23T18:00:00",
            "programa_id": 1
        },
        {
            "data_fim": "2018-10-24T20:00:00",
            "data_inicio": "2018-10-24T18:00:00",
            "programa_id": 1
        },
        {
            "data_fim": "2018-10-25T22:00:00",
            "data_inicio": "2018-10-25T18:00:00",
            "programa_id": 1
        },
        {
            "data_fim": "2018-10-26T18:00:00",
            "data_inicio": "2018-10-26T11:00:00",
            "programa_id": 1
        }
    ],
    [
        {
            "data_fim": "2018-10-26T20:00:00",
            "data_inicio": "2018-10-26T12:00:00",
            "programa_id": 3
        },
    ],
    [
        {
            "data_fim": "2018-10-23T20:00:00",
            "data_inicio": "2018-10-23T18:00:00",
            "programa_id": 2
        },
        {
            "data_fim": "2018-10-25T22:00:00",
            "data_inicio": "2018-10-25T18:00:00",
            "programa_id": 2
        }
    ],
    [
        {
            "data_fim": "2018-10-22T20:00:00",
            "data_inicio": "2018-10-22T18:00:00",
            "programa_id": 4
        },
        {
            "data_fim": "2018-10-24T20:00:00",
            "data_inicio": "2018-10-24T18:00:00",
            "programa_id": 4
        },
        {
            "data_fim": "2018-10-26T22:00:00",
            "data_inicio": "2018-10-26T18:00:00",
            "programa_id": 4
        }
    ]
]

print timezone.now()


class TestCase(TestCase):
    """
    Realiza o teste utilizando request a API e avaliando seu retorno
    """

    def setUp(self):
        self.c = Client()

        radio_obj = []
        for radio in RADIOS:
            radio_aux = Radio(**radio)
            radio_aux.save()
            radio_obj.append(radio_aux)

        categoria_obj = []
        for categoria in CATEGORIAS:
            categoria_aux = Categoria(**categoria)
            categoria_aux.save()
            categoria_obj.append(categoria_aux)


        programa_obj = []
        for programa in PROGRAMAS:
            programa_aux = Programa(**programa)
            programa_aux.save()
            programa_obj.append(programa_aux)

        programacao_obj = []
        for programacao in PROGRAMACAO:
            for horario in programacao:
                programacao_aux = Programacao(**horario)
                programacao_aux.save()
                programa_obj.append(programacao_aux)



    def test_prioridade(self):
        from django.utils import timezone
        #print timezone.now()
        response = self.c.get("/api/v1/aovivo/")
        objects = response.json()["objects"]
       

        self.assertEqual(objects[0]['programa']["id"], 3)
