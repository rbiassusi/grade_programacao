from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api
from radio.api.resources import ProgramaResource
from radio.api.resources import ProgramacaoResource, ProgramCompletoResource
from radio.api.resources import AoVivoResource
from radio.api.resources import RadioResource
from radio.api.resources import CategoriaResource

v1_api = Api(api_name='v1')

v1_api.register(ProgramaResource())
v1_api.register(ProgramacaoResource())
v1_api.register(AoVivoResource())
v1_api.register(RadioResource())
v1_api.register(CategoriaResource())
v1_api.register(ProgramCompletoResource())

urlpatterns = [
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', admin.site.urls),
]
