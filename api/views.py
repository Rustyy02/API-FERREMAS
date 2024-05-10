from rest_framework import viewsets
from .serializer import ProductoSerializer,CompraSerializer,SolicitudSerializer,ClienteSerializer,ContadorSerializer,BodegueroSerializer,VendedorSerializer
from .models import Producto,Compra,Solicitud,Cliente,Contador,Bodeguero,Vendedor
from .forms import ProductoForm, CompraForm, SolicitudForm,ClienteForm,ContadorForm,BodegueroForm,VendedorForm
from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
import random

#GESTION USUARIOS
def vistaAdmin(request):
    return render(request, 'vistaAdmin/vistaAdmin.html')

def home(request):
    return render(request,'home.html')


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
def crear_sesion(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = ClienteForm()
    return render(request, 'vistaCliente/crear_sesion.html', {'form': form})
    
class ContadorViewSet(viewsets.ModelViewSet):
    queryset = Contador.objects.all()
    serializer_class = ContadorSerializer
    
def crear_contador(request):
    if request.method == 'POST':
        form = ContadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vistaAdmin')
    else:
        form = ContadorForm()
    return render(request, 'vistaContador/crear_contador.html', {'form': form})

def lista_despachos(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'vistaContador/lista_despachos.html', {'solicitudes': solicitudes}) 

def ver_despacho(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    return render(request, 'vistaContador/ver_despacho.html', {'solicitud': solicitud})

def actualizar_pedido(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if request.method == 'POST':
        form = SolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('lista_despachos')
    else:
        form = SolicitudForm(instance=solicitud)
    return render(request, 'vistaContador/actualizar_pedido.html', {'form': form})

class BodegueroViewSet(viewsets.ModelViewSet):
    queryset = Bodeguero.objects.all()
    serializer_class = BodegueroSerializer
    
def crear_bodeguero(request):
    if request.method == 'POST':
        form = BodegueroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vistaAdmin')
    else:
        form = BodegueroForm()
    return render(request, 'vistaBodeguero/crear_bodeguero.html', {'form': form})

def despachar(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if request.method == 'POST':
        form = SolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('solicitudes')
    else:
        form = SolicitudForm(instance=solicitud)
    return render(request, 'vistaBodeguero/despachar.html', {'form': form})
    
class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

def crear_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vistaAdmin')
    else:
        form = VendedorForm()
    return render(request, 'vistaVendedor/crear_vendedor.html', {'form': form})
#CRUD PRODUCTOS
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'vistaAdmin/lista_productos.html', {'productos': productos})   

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'vistaAdmin/crear_producto.html', {'form': form})#hacer la vista

def borrar_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'vistaAdmin/borrar_productos.html', {'producto': producto})

def editar_productos(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'vistaAdmin/editar_productos.html', {'form': form})

#PROCESO DE COMPRA
#Ventas
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'vistaCliente/catalogo.html', {'productos': productos})    

def ver_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'vistaCliente/ver_detalle.html', {'producto': producto})


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    
def lista_compras(request):
    compras = Compra.objects.all()
    return render(request, 'vistaVendedor/lista_compras.html', {'compras': compras}) 

def ver_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    return render(request, 'vistaVendedor/ver_compra.html', {'compra': compra})
    
def crear_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = CompraForm()
    return render(request, 'vistaCliente/crear_compra.html', {'form': form})

def rechazar_compra(request, pk):
    compra = get_object_or_404(Compra, pk=pk)
    if request.method == 'POST':
        compra.delete()
        return redirect('lista_compras')
    return render(request, 'vistaVendedor/rechazar_compra.html', {'compra': compra})




#SOLICITUDES
class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
    
def solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'vistaBodeguero/solicitudes.html', {'solicitudes': solicitudes}) 
    
def ver_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    return render(request, 'vistaBodeguero/ver_solicitud.html', {'solicitud': solicitud})

def crear_solicitud(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('solicitudes')
    else:
        form = SolicitudForm()
    return render(request, 'vistaVendedor/crear_solicitud.html', {'form': form})

def despachar(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if request.method == 'POST':
        form = SolicitudForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('solicitudes')
    else:
        form = SolicitudForm(instance=solicitud)
    return render(request, 'vistaBodeguero/despachar.html', {'form': form})

def rechazar_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('solicitudes')
    return render(request, 'vistaBodeguero/rechazar_solicitud.html', {'solicitud': solicitud})


