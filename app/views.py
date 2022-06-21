import re
from django.shortcuts import render
from .models import medicamentocompra
from .models import medicamento , fichapaciente


# Create your views here.
def index(request):
    return render(request, 'app/index.html' )
def contacto(request):
    return render(request, 'app/contacto.html' )
def lista_productos(request):
    medicamentoscompra = medicamentocompra.objects.all()
    data = {
       'medicamentoscompra':medicamentoscompra
    }
    return render(request, 'app/lista_productos.html' ,data)
def login(request):
    return render(request, 'app/login.html' )
def lista_paciente(request):
    fichapacientes = fichapaciente.objects.all()
    data = {
        'fichapacientes' :fichapacientes
    }
    
    return render(request, 'app/lista_paciente.html' ,data)
def lista_medicamentos(request):
    medicamentos = medicamento.objects.all()
    data = {
        'medicamentos' :medicamentos
    }
    return render(request, 'app/lista_medicamentos.html', data )