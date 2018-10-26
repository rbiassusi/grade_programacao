# coding: utf-8
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from ...models import Programa


class ProgramaResource(ModelResource):
    #categoria = fields.ForeignKey(
    #    'radio.api.resources.CategoriaResource', 'categoria', full=True)
    #horarios = fields.ToManyField(
    #    'radio.api.resources.ProgramacaoResource', 'horarios', related_name="programa", null=True, blank=True, full=True)
    radio = fields.ForeignKey(
        'radio.api.resources.RadioResource', 'radio', full=True)

    class Meta:
        queryset = Programa.objects.all()
        resource_name = 'programa'
        authorization = Authorization()
        filtering = {
            'radio': ALL_WITH_RELATIONS,
        }

class ProgramCompletoResource(ModelResource):
    categoria = fields.ForeignKey(
        'radio.api.resources.CategoriaResource', 'categoria', full=True)
    horarios = fields.ToManyField(
        'radio.api.resources.ProgramaHorariosResource', 'horarios', related_name="programa", null=True, blank=True, full=True)
    radio = fields.ForeignKey(
        'radio.api.resources.RadioResource', 'radio', full=True)

    class Meta:
        queryset = Programa.objects.all()
        resource_name = 'programa_completo'
        authorization = Authorization()
        filtering = {
            'radio': ALL_WITH_RELATIONS,
        }        

