from django import forms
from .models import  Producto,Compra,Solicitud,Cliente,Contador,Bodeguero,Vendedor

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
              
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'
   
#sesiones
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ContadorForm(forms.ModelForm):
    class Meta:
        model = Contador
        fields = '__all__'

class BodegueroForm(forms.ModelForm):
    class Meta:
        model = Bodeguero
        fields = '__all__'
        
class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'     
        