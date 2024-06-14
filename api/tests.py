from django.test import TestCase, Client
from django.urls import reverse
from . import models
from .factories import MyModelFactory
import factory

class MyModelIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.mymodel1 = MyModelFactory(codigoProducto = factory.Sequence(lambda n: f'prueba1{n}'),
    nombre = factory.Sequence(lambda n: n),
    marca = factory.Sequence(lambda n: f'prueba1{n}'),
    precio = factory.Sequence(lambda n: n),
    stock_estado = factory.Sequence(lambda n: n),
    stock_cantidad = factory.Sequence(lambda n: n))
        

    def prueba_vista_modelo_Producto(self):
        """Prueba la vista de lista de MyModel"""
        response = self.client.get(reverse('Producto_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ferreteria/Producto_list.html')
        self.assertContains(response, 'test1')
        self.assertContains(response, 'test2')

    def test_mymodel_create_view_get(self):
        """Prueba el acceso GET a la vista de creación de MyModel"""
        response = self.client.get(reverse('Producto_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ferreteria/ProductoForm.html')

    def test_mymodel_create_view_post(self):
        """Prueba la creación de MyModel a través de la vista de creación"""
        response = self.client.post(reverse('Producto_create'), {
            
            'codigoProducto': 3,
            'nombre': 'Martillo',
            'marca': 'Bauker',
            'precio': 6000,
            'stock_estado': True,
            'stock_cantidad': 6

        })
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('Producto_list'))
        self.assertEqual(models.Producto.objects.count(), 3)
        self.assertTrue(models.Producto.objects.filter(name='test3').exists())
