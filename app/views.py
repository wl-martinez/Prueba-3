from django.shortcuts import render
from .models import Producto

# Create your views here.

def productos(request):
    productos = Producto.objects.all()
    data = {
         'productos': productos
    }
    return render(request, 'app/productos.html', data)

def carrito(request):
    carrito = Producto.objects.all()
    data = {
         'carrito': carrito
    }
    return render(request, 'app/carrito.html')

def ingresar(request):
    ingresar = Producto.objects.all()
    data = {
         'ingresar': ingresar
    }
    return render(request, 'app/ingresar.html')

def index(request):
    index = Producto.objects.all()
    data = {
         'index': index
    }
    return render(request, 'app/index.html')

