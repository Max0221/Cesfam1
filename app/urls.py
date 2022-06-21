from django.urls import path
from .views import index,contacto,lista_productos,login,lista_paciente,lista_medicamentos

urlpatterns = [
    path('',index,  name="index"),
    path('contacto/',contacto,  name="contacto"),
    path('lista_productos/',lista_productos,  name="lista_producto"),
    path('login/', login ,  name="login"),
    path('lista_paciente/', lista_paciente ,  name="lista_paciente"),
    path('lista_medicamentos/', lista_medicamentos, name="lista_medicamentos",)
]
