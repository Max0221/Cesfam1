import email
from django.contrib import admin
from .models import medicamento, fichapaciente, medicamentocompra

class FichaPacienteAdmin(admin.ModelAdmin):
    list_display = ["nombre","imagen","rut","email","numero","descripcion","medicamento"]
    search_fields = ["rut"]

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ["nombre","stock","fecha_fabricacion","caducado"]
    list_editable = ["caducado"]
    search_fields = ["nombre"]


# Register your models here.
admin.site.register(medicamentocompra)
admin.site.register(fichapaciente,FichaPacienteAdmin)
admin.site.register(medicamento,MedicamentoAdmin)