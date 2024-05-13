"""
URL configuration for ferreteria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('', views.home, name='home'),
    path('vistaAdmin/', views.vistaAdmin, name='vistaAdmin'),
    
    path('api-auth/', include('rest_framework.urls')),
    #usuarios
    path('vistaCliente/crear_sesion/', views.crear_sesion, name='crear_sesion' ),
    path('vistaVendedor/crear_vendedor/', views.crear_vendedor, name='crear_vendedor' ),
    path('vistaBodeguero/crear_bodeguero/', views.crear_bodeguero, name='crear_bodeguero' ),
    path('vistaContador/crear_contador/', views.crear_contador, name='crear_contador' ),
    #VISTA ADMIN CRUD
    path('vistaAdmin/crear_producto/', views.crear_producto, name='crear_producto' ),
    path('vistaAdmin/lista_productos/', views.lista_productos, name='lista_productos'),
    path('vistaAdmin/borrar_productos/<int:pk>/', views.borrar_productos, name='borrar_productos'),
    path('vistaAdmin/editar_productos/<int:pk>/', views.editar_productos, name='editar_productos'),
    
    #COMPRA Y PRODUCTOS VISTA CLIENTE
    path('vistaCliente/catalogo/', views.catalogo, name='catalogo'),
    path('vistaCliente/ver_detalle/<int:pk>/', views.ver_detalle, name='ver_detalle'),
    #COMPRAS VISTA VENDEDOR
    path('vistaVendedor/crear_compra/', views.crear_compra, name='crear_compra' ),
    path('vistaVendedor/lista_compras/', views.lista_compras, name='lista_compras'),
    path('vistaVendedor/ver_compra/<int:pk>/', views.ver_compra, name='ver_compra'),
    path('vistaVendedor/rechazar_compra/<int:pk>/', views.rechazar_compra, name='rechazar_compra'),
    #SOLICITUDES VISTA BODEGUERO
    path('vistaBodeguero/crear_solicitud/', views.crear_solicitud, name='crear_solicitud' ),
    path('vistaBodeguero/solicitudes/', views.solicitudes, name='solicitudes'),
    path('vistaBodeguero/ver_solicitud/<int:pk>/', views.ver_solicitud, name='ver_solicitud'),
    path('vistaBodeguero/despachar/<int:pk>/', views.despachar, name='despachar'),
    path('vistaBodeguero/rechazar_solicitud/<int:pk>/', views.rechazar_solicitud, name='rechazar_solicitud'),
    #VISTA CONTADOR
    path('vistaContador/lista_despachos/', views.lista_despachos, name='lista_despachos'),
    path('vistaContador/ver_despacho/<int:pk>/', views.ver_despacho, name='ver_despacho'),
    path('vistaContador/actualizar_pedido/<int:pk>/', views.actualizar_pedido, name='actualizar_pedido'),
]
