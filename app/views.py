import re
from django.shortcuts import render
from .models import medicamentocompra

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