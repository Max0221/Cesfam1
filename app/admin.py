from django.contrib import admin
from .models import medicamento, fichapaciente, medicamentocompra

# Register your models here.
admin.site.register(medicamentocompra)
admin.site.register(fichapaciente)
admin.site.register(medicamento)