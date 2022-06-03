from django.urls import path
from .views import index,contacto,lista_productos

urlpatterns = [
    path('',index,  name="index"),
    path('contacto/',contacto,  name="contacto"),
    path('lista_productos/',lista_productos,  name="lista_producto")
]
