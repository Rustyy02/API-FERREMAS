from django.contrib import admin
from .models import Producto,Compra,Solicitud,Cliente,Contador,Bodeguero,Vendedor
# Register your models here.

admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(Solicitud)

admin.site.register(Cliente)
admin.site.register(Contador)
admin.site.register(Bodeguero)
admin.site.register(Vendedor)