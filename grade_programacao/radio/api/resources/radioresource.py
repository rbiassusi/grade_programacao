# coding: utf-8
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.validation import FormValidation
from ...models import Radio
from ...forms import RadioForm

class RadioResource(ModelResource):
    class Meta:
        queryset = Radio.objects.all()
        resource_name = 'radio'
        authorization = Authorization()
        validation = FormValidation(form_class=RadioForm)

        