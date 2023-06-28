from django.urls import path
from .views import index, carrito, ingresar, productos
urlpatterns = [
    path('', index, name="index"),
    path('carrito/', carrito, name="carrito"),
    path('ingresar/', ingresar, name="ingresar"),
    path('productos/', productos, name="productos"),
]


