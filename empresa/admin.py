from django.contrib import admin
from .models import Tecnologias, Empresa, Vagas, Profissao

admin.site.register(Tecnologias)
admin.site.register(Profissao)
admin.site.register(Empresa)
admin.site.register(Vagas)
