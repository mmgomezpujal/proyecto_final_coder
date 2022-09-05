from unicodedata import name
from django.urls import path
from AppTienda import views

urlpatterns = [
    path('nuevo-cliente/', views.clientes_formulario, name='Formulario Cliente'),
    path('nuevo-distribuidor/', views.distribuidores_formulario, name='Formulario Distribuidor'),
    path('post-venta/',views.postventa_formulario, name='Nuevo Reclamo'),
    path('buscar-distribuidor/', views.busqueda_distribuidor, name="Buscar Distribuidor"),
    path('buscar/', views.buscar),
    path('', views.inicio, name='Inicio'),
    path('clientes/', views.clientes, name='Clientes'),
    path('distribuidores/', views.distribuidores, name='Distribuidores'),
    path('postventa/', views.post_venta, name='Post Venta'),
]
