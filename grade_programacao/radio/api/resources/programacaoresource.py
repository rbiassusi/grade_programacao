# coding: utf-8
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from ...models import Programacao
from django.utils import timezone

class ProgramacaoResource(ModelResource):
    programa = fields.ForeignKey('radio.api.resources.ProgramaResource', 'programa', full=True)
    class Meta:
        queryset = Programacao.objects.all()
        resource_name = 'programacao'
        authorization = Authorization()
        fields = ['data_inicio', 'data_fim'] 
        filtering = {
            'programa': ALL_WITH_RELATIONS,
        }        


class AoVivoResource(ModelResource):
    programa = fields.ForeignKey('radio.api.resources.ProgramaResource', 'programa', full=True)    
    class Meta:
        queryset = Programacao.objects.filter(data_inicio__lte=timezone.now(), data_fim__gte=timezone.now()).order_by('-programa__categoria__ordem_prioridade')
        #queryset = Programacao.objects.filter(data_fim__gte=datetime.datetime.now())
        resource_name = 'aovivo'
        authorization = Authorization()
        filtering = {
            'programa': ALL_WITH_RELATIONS,
    }


class ProgramaHorariosResource(ModelResource):
    #programa = fields.ForeignKey('radio.api.resources.ProgramaResource', 'programa', full=True)  
    class Meta:
        queryset = Programacao.objects.all()
        resource_name = 'programacao'
        authorization = Authorization()
        fields = ['data_inicio', 'data_fim'] 
        filtering = {
            'programa': ALL_WITH_RELATIONS,
        }       
