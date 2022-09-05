from http.client import HTTPResponse
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.http import HttpResponse
from AppTienda.models import*
from AppTienda.forms import*


from AppTienda.forms import ClientesFormulario

def clientes(request):
    return render (request, 'AppTienda/clientes.html')


def distribuidores(request):
    return render (request, 'AppTienda/distribuidores.html')


def inicio(request):
    return render (request, 'AppTienda/inicio.html')


def post_venta(request):
    return render (request, 'AppTienda/postventa.html')

def clientes_formulario(request):
    if request.method == 'POST':
        formulario_1 = ClientesFormulario(request.POST)
        if formulario_1.is_valid():
            data_1 = formulario_1.cleaned_data
            clientes = Clientes(nombre=data_1['nombre'], apellido=data_1['apellido'], email=data_1['email'])
            clientes.save()
            return render(request, 'AppTienda/inicio.html')
    else:
        formulario_1 = ClientesFormulario()
        return render(request, 'AppTienda/form_clientes.html', {'formulario_1': formulario_1})


def distribuidores_formulario(request):
    if request.method == 'POST':
        formulario_2 = DistribuidoresFormulario(request.POST)
        if formulario_2.is_valid():
            data_2 = formulario_2.cleaned_data
            distribuidores = Distribuidores(nombre=data_2['nombre'], apellido=data_2['apellido'], direccion= data_2['direccion'], email=data_2['email'])
            distribuidores.save()
            return render(request, 'AppTienda/inicio.html')
    else:
        formulario_2 = DistribuidoresFormulario()
        return render(request, 'AppTienda/form_distribuidores.html', {'formulario_2': formulario_2})


def postventa_formulario(request):
    if request.method == 'POST':
        formulario_3 = PostVentaFormulario(request.POST)
        if formulario_3.is_valid():
            data_3 = formulario_3.cleaned_data
            postventa = PostVenta(nombre=data_3['nombre'], apellido=data_3['apellido'], email=data_3['email'], fecha=data_3['fecha'], producto=data_3['producto'],descripcion_reclamo=['descripcion_reclamo'])
            postventa.save()
            return render(request, 'AppTienda/inicio.html')
    else:
        formulario_3 = PostVentaFormulario()
        return render(request, 'AppTienda/form_postventa.html', {'formulario_3': formulario_3})


# Create your views here.
