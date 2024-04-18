from django.contrib import admin
from .models import Especialidade
from .models import DadosMedico
from .models import DatasAbertas

admin.site.register(Especialidade)
admin.site.register(DadosMedico)
admin.site.register(DatasAbertas)
