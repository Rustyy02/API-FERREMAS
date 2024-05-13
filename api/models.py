from django.db import models

# Create de todo asociado a productos.
class Producto(models.Model):
    codigoProducto = models.BigAutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=80)
    marca = models.CharField(max_length=50)
    precio = models.PositiveBigIntegerField()
    stock_estado = models.BooleanField(default=True)
    stock_cantidad = models.PositiveIntegerField(default=100)
    
    
class Compra(models.Model):
    METODO_ENTREGA = {
        "D": "Despacho a Domicilio",
        "R": "Retiro en Tienda",
    }
    METODO_PAGO = {
        "C": "Credito",
        "D": "Debito",
        "E": "Efectivo",
    }
    product = models.ForeignKey(Producto,null=True,blank=True,on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField()
    metodo_pago = models.CharField(max_length=1, choices=METODO_PAGO) 
    metodo_entrega = models.CharField(max_length=1, choices=METODO_ENTREGA,default="Despacho a Domicilio") 

class Solicitud(models.Model):
    ESTADO_PEDIDO = {
        "P": "Pedido en Proceso",
        "R": "Pedido rechazado",
        "E": "Pedido enviado",
        "D": "Pedido Despachado"
    }
    soli = models.ForeignKey(Compra,null=True,blank=True,on_delete=models.CASCADE)
    estado_pedido = models.CharField(max_length=1, choices=ESTADO_PEDIDO) 
    pago_realizado= models.BooleanField(default=True)
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveBigIntegerField()
    celular = models.PositiveBigIntegerField()
    correo = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    
class Contador(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveBigIntegerField()
    celular = models.PositiveBigIntegerField()
    correo = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)

class Bodeguero(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveBigIntegerField()
    celular = models.PositiveBigIntegerField()
    correo = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
   
class Vendedor(models.Model):
    CARGO = {
        "C": "Cajero",
        "V": "Vendedor",
        "S": "Supervisor",
    }
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveBigIntegerField()
    celular = models.PositiveBigIntegerField()
    correo = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    cargo = models.CharField(max_length=1, choices=CARGO)
    