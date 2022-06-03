import re
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html' )
def contacto(request):
    return render(request, 'app/contacto.html' )
def lista_productos(request):
    return render(request, 'app/lista_productos.html' )