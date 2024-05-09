from rest_framework import viewsets
from .serializer import ProductoSerializer,CompraSerializer,SolicitudSerializer,ClienteSerializer,ContadorSerializer,BodegueroSerializer,VendedorSerializer
from .models import Producto,Compra,Solicitud,Cliente,Contador,Bodeguero,Vendedor

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
import random


#Ventas
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos})    

def ver_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'ver_detalle.html', {'producto': producto})

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
    
#usuarios
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
class ContadorViewSet(viewsets.ModelViewSet):
    queryset = Contador.objects.all()
    serializer_class = ContadorSerializer

class BodegueroViewSet(viewsets.ModelViewSet):
    queryset = Bodeguero.objects.all()
    serializer_class = BodegueroSerializer
    
class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
# Create your views here.
