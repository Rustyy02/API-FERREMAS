import factory
from . import models

class MyModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Producto

    codigoProducto = factory.Sequence(lambda n: f'prueba1{n}')
    nombre = factory.Sequence(lambda n: n)
    marca = factory.Sequence(lambda n: f'prueba1{n}')
    precio = factory.Sequence(lambda n: n)
    stock_estado = factory.Sequence(lambda n: n)
    stock_cantidad = factory.Sequence(lambda n: n)