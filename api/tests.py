from django.test import TestCase, Client
from django.urls import reverse
from . import models
from .models import Producto,Compra,Solicitud,Cliente,Contador,Bodeguero,Vendedor
from .factories import MyModelFactory
import factory

#PRODUCTO
class ProductoIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.producto1 = Producto.objects.create(codigoProducto=6,nombre="Destornillador",marca="Baunker",precio=7000,stock_estado=True,stock_cantidad=4)

    def test_vista_modelo_Producto(self):
        """Prueba la vista de lista de MyModel"""
        response = self.client.get(reverse('lista_productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vistaAdmin/lista_productos.html')
        self.assertContains(response, 'Destornillador')

    def test_mymodel_create_view_get(self):
        """Prueba el acceso GET a la vista de creación de MyModel"""
        response = self.client.get(reverse('crear_producto'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vistaAdmin/crear_producto.html')

    def test_mymodel_create_view_post(self):
        """Prueba la creación de MyModel a través de la vista de creación"""
        response = self.client.post(reverse('crear_producto'), {
            
                'codigoProducto': 7,
                'nombre': 'Martillo',
                'marca': 'Baunker',
                'precio': 5000,
                'stock_estado': True,
                'stock_cantidad': 4

        })
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lista_productos'))
        self.assertEqual(models.Producto.objects.count(), 2)
        self.assertTrue(models.Producto.objects.filter(nombre='Martillo').exists())

#COMPRA
class CompraIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.producto1 = Producto.objects.create(codigoProducto=6,nombre="Destornillador",marca="Baunker",precio=7000,stock_estado=True,stock_cantidad=4)

    def create_compra_test(self):
        self.client = Client()
        self.compra1 = Compra.objects.create(product=self.producto1,cantidad=6,metodo_pago="C",metodo_entrega="R")

        response = self.client.get(reverse('lista_compras'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vistaVendedor/lista_compras/')
        self.assertContains(response, 'compra1')

    def test_compra_create_view_get(self):
        """Prueba el acceso GET a la vista de creación de Compra"""
        response = self.client.get(reverse('crear_compra'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vistaCliente/crear_compra.html')

    def test_compra_create_view_post(self):
        """Prueba la creación de Compra a través de la vista de creación"""
        response = self.client.post(reverse('crear_compra'), {
            'product': self.producto1.codigoProducto,  # Pasa el ID del producto en lugar de la instancia
            'cantidad': 8,
            'metodo_pago': 'C',
            'metodo_entrega': 'R'
        })
        if response.status_code != 302:
            print(response.context['form'].errors)     
        
        self.assertEqual(response.status_code, 302)  # El status code debería ser 302 para una redirección
        self.assertRedirects(response, reverse('lista_compras'))
        self.assertEqual(Compra.objects.count(), 1)
        self.assertTrue(Compra.objects.filter(product=self.producto1).exists())


#SOLICITUDEEEES  
class SolicitudIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.producto1 = Producto.objects.create(codigoProducto=6,nombre="Destornillador",marca="Baunker",precio=7000,stock_estado=True,stock_cantidad=4)

    def create_compra_test(self):
        self.client = Client()
        self.compra1 = Compra.objects.create(product=self.producto1,cantidad=6,metodo_pago="C",metodo_entrega="R")
    
    
    def create_solicitudes_test(self):
        self.client = Client()
        self.soli1 = Solicitud.objects.create(soli=self.compra1,estado_pedido="R",pago_realizado=True)

        response = self.client.get(reverse('solicitudes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vistaBodeguero/solicitudes/')
        self.assertContains(response, 'soli1')

    def test_solicitudes_create_view_get(self):
        """Prueba el acceso GET a la vista de creación de solicitudes"""
        response = self.client.get(reverse('crear_solicitud'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vistaBodeguero/solicitudes.html')

    def test_solicitudes_create_view_post(self):
        """Prueba la creación de solicitudes a través de la vista de creación"""
        response = self.client.post(reverse('crear_solicitud'), {
            'soli': self.compra1,  # Pasa el ID del producto en lugar de la instancia
            'estado_pedido': "P",
            'pago_realizado': False
        })
        if response.status_code != 302:
            print(response.context['form'].errors)     
        
        self.assertEqual(response.status_code, 302)  # El status code debería ser 302 para una redirección
        self.assertRedirects(response, reverse('solicitudes'))
        self.assertEqual(Solicitud.objects.count(), 2)
        self.assertTrue(Solicitud.objects.filter(soli=self.compra1).exists())
        
#cliente
class ClienteIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.producto1 = Cliente.objects.create(nombre = "Martin",
        apellido = "casas",
        edad = 20,
        celular = 942909645,
        correo = "martin@duocuc.cl",
        direccion = "ojos de agua"
    )

    def test_mymodel_create_view_get(self):
        """Prueba el acceso GET a la vista de creación de cliente"""
        response = self.client.get(reverse('crear_sesion'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vistaCliente/crear_sesion.html')

    def test_mymodel_create_view_post(self):
        """Prueba la creación de cliente a través de la vista de creación"""
        response = self.client.post(reverse('crear_sesion'), {
            
            'nombre' : "Martin",
            'apellido' : "casas",
            'edad' : 22,
            'celular' : 942909645,
            'correo' : "sergio@duocuc.cl",
            'direccion' : "valpo"

        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Cliente.objects.count(), 2)
        self.assertTrue(models.Cliente.objects.filter(nombre='Martin').exists())
#vendedor
class VendedorIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.producto1 = Vendedor.objects.create(nombre = "Martin",
        apellido = "casas",
        edad = 20,
        celular = 942909645,
        correo = "martin@duocuc.cl",
        direccion = "ojos de agua",
        cargo = "C"
    )

    def test_mymodel_create_view_get(self):
        """Prueba el acceso GET a la vista de creación de Vendedor"""
        response = self.client.get(reverse('crear_vendedor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vistaVendedor/crear_vendedor.html')

    def test_mymodel_create_view_post(self):
        """Prueba la creación de Vendedor a través de la vista de creación"""
        response = self.client.post(reverse('crear_vendedor'), {
            
            'nombre' : "Martin",
            'apellido' : "casas",
            'edad' : 22,
            'celular' : 942909645,
            'correo' : "sergio@duocuc.cl",
            'direccion' : "valpo",
            'cargo': "V"

        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Vendedor.objects.count(), 2)
        self.assertTrue(models.Vendedor.objects.filter(nombre='Martin').exists())    
#bodeguero
class BodegueroIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.producto1 =  Bodeguero.objects.create(nombre = "Martin",
        apellido = "casas",
        edad = 20,
        celular = 942909645,
        correo = "martin@duocuc.cl",
        direccion = "ojos de agua"
    )

    def test_Bodeguero_create_view_get(self):
        """Prueba el acceso GET a la vista de creación de  Bodeguero"""
        response = self.client.get(reverse('crear_bodeguero'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vistaBodeguero/crear_bodeguero.html')

    def test_Bodeguero_create_view_post(self):
        """Prueba la creación de  Bodeguero a través de la vista de creación"""
        response = self.client.post(reverse('crear_bodeguero'), {
            
            'nombre' : "Martin",
            'apellido' : "casas",
            'edad' : 22,
            'celular' : 942909645,
            'correo' : "sergio@duocuc.cl",
            'direccion' : "valpo"

        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Bodeguero.objects.count(), 2)
        self.assertTrue(models.Bodeguero.objects.filter(nombre='Martin').exists())
#contador
class ContadorIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.producto1 = Contador.objects.create(nombre = "Martin",
        apellido = "casas",
        edad = 20,
        celular = 942909645,
        correo = "martin@duocuc.cl",
        direccion = "ojos de agua"
    )

    def test_Contador_create_view_get(self):
        """Prueba el acceso GET a la vista de creación de Contador"""
        response = self.client.get(reverse('crear_contador'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vistaContador/crear_contador.html')

    def test_Contador_create_view_post(self):
        """Prueba la creación de Contador a través de la vista de creación"""
        response = self.client.post(reverse('crear_contador'), {
            
            'nombre' : "Martin",
            'apellido' : "casas",
            'edad' : 22,
            'celular' : 942909645,
            'correo' : "sergio@duocuc.cl",
            'direccion' : "valpo"

        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Contador.objects.count(), 2)
        self.assertTrue(models.Contador.objects.filter(nombre='Martin').exists())
