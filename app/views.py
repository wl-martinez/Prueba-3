from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm
from .models import Producto

# Create your views here.

def crear_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = UserForm()
    
    return render(request, 'admin/crear_usuario.html', {'form': form})
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

