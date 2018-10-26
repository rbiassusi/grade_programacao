# coding: utf-8
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.validation import FormValidation
from ...models import Categoria
from ...forms import CategoriaForm

class CategoriaResource(ModelResource):
    class Meta:
        queryset = Categoria.objects.all()
        resource_name = 'categoria'
        authorization = Authorization()
        fields = ['nome', 'id'] 
        validation = FormValidation(form_class=CategoriaForm)
        