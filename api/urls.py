from django.urls import path,include
from rest_framework import routers
from api import views

router= routers.DefaultRouter()
router.register(r'producto', views.ProductoViewSet)
router.register(r'solicitud', views.SolicitudViewSet)
router.register(r'compra', views.CompraViewSet)

router.register(r'cliente', views.ClienteViewSet)
router.register(r'contador', views.ContadorViewSet)
router.register(r'bodeguero', views.BodegueroViewSet)
router.register(r'vendedor', views.VendedorViewSet)

urlpatterns = [
    path('',include(router.urls))
]
