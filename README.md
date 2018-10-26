# grade_programacao
Grade de programação

API para um serviço de grade de programação

Requisitos
==========

Core
----
* Python 2.7
* Django 1.11
* Tastypie

Opcional
--------
* pip
* virtual_env 

Instalação
==========
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py createsuperuser (para acesso ao /admin)

Teste
=====
* python manage.py test

Utilização
==========
Rodar o servidor django:
* python manage.py runserver

1. Acesso a interface admin:
* http://localhost:8000/admin
preencha usuario e senha criados no comando "python manage.py createsuperuser"


------

2. Acesso via API

* Endereço da API:
  /api/v1
  
  
* Endpoint e Schema:
aovivo:
(list_endpoint: /api/v1/aovivo/)
(schema: /api/v1/aovivo/schema/)
    
categoria:
(list_endpoint: /api/v1/categoria/)
(schema: /api/v1/categoria/schema/)

programa:
(list_endpoint: /api/v1/programa/)
(schema: /api/v1/programa/schema/)

programa_completo:
(list_endpoint: /api/v1/programa_completo/)
(schema: /api/v1/programa_completo/schema/)

programacao:
(list_endpoint: /api/v1/programacao/)
(schema: /api/v1/programacao/schema/)

radio:
(list_endpoint: /api/v1/radio/)
(schema: /api/v1/radio/schema/)
    


* Melhorias futuras:
Melhorar a forma de teste com horarios dinamicos.
