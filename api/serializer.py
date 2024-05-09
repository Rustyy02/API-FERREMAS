from rest_framework import serializers
from .models import Producto,Compra,Solicitud,Cliente,Contador,Bodeguero,Vendedor

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ContadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contador
        fields = '__all__'
        
class BodegueroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodeguero
        fields = '__all__'
    
class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'