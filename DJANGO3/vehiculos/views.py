from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

import vehiculos

from .models import carros

# Create your views here.

def inicio(request):

    plantilla = loader.get_template("inicio.html")
    documento = plantilla.render( )
    
    return HttpResponse( documento )

def saludar(request):
    
    return HttpResponse("Bienvenido a mi primer URL")

def crear_estatico(request):
    
    objeto = carros( marca = "Mazda" , color = "Blanco" , cantidad_pasajeros = 5 , fecha_salida = "2021-11-13" )
    objeto.save()
    
    return HttpResponse("Datos cargados con exito")

def crear_dinamico(request):
    
    if request.GET:
        
        marcas = str( request.GET['marcas'] )
        
        colores = str( request.GET['colores'] )
        
        cantidad = int( request.GET['cantidad'] )
        
        fecha = str( request.GET['fecha'] )
        
        objeto2 = carros( marca = marcas , color = colores , cantidad_pasajeros = cantidad , fecha_salida = fecha )
        objeto2.save()
    
    
    info = carros.objects.all()
    
    contexto = { "vehiculos" : info }
    
    plantilla = loader.get_template("crear.html")
    documento = plantilla.render( contexto )
    
    
    return HttpResponse( documento )
        
def mostrar(request):
    
    info = carros.objects.all()
    contexto = { "vehiculos" : info }
    
    plantilla = loader.get_template("mostrar.html")
    documento = plantilla.render( contexto )
    
    return HttpResponse( documento )

def CRUD(request):

    info = carros.objects.all()
    contexto = { "vehiculos" : info }

    plantilla = loader.get_template("CRUD.html")
    documento = plantilla.render( contexto )
    
    return HttpResponse( documento )

def detail(request, id):

    detail_vehiculos = get_object_or_404(carros, pk = id)
    contexto = { "detalles" : detail_vehiculos }

    plantilla = loader.get_template("detail.html")
    documento = plantilla.render( contexto )
    
    return HttpResponse( documento )

def actualizar(request, id2):
    carro2 = carros.objects.get(id = int(id2))

    if request.GET:
        
        carro2.marca = str( request.GET['marcas'] )
        
        carro2.color = str( request.GET['colores'] )
        
        carro2.cantidad_pasajeros = int( request.GET['cantidad'] )
        
        carro2.fecha_salida = str( request.GET['fecha'] )

        carro2.save()

        info = carros.objects.all()
        contexto = { "vehiculos" : info }

        plantilla = loader.get_template("CRUD.html")
        documento = plantilla.render( contexto )
    
        return HttpResponse( documento )

    
    plantilla = loader.get_template("editar.html")
    documento = plantilla.render( )
    
    return HttpResponse( documento )

def borrar(request, id2):

    carro2 = carros.objects.get(id = int(id2))
    carro2.delete()

    info = carros.objects.all()
    contexto = { "vehiculos" : info }

    plantilla = loader.get_template("CRUD.html")
    documento = plantilla.render( contexto )
    
    return HttpResponse( documento )

def buscar(request):

    var2 = carros.objects.all()
    contexto = { "todos" : var2 }

    if request.GET:

        buscador = carros.objects.filter(marca__icontains = request.GET["buscar"])

        contexto = { "buscados" : buscador , "todos" : var2 }

        plantilla = loader.get_template("buscador.html")
        documento = plantilla.render( contexto )
        return HttpResponse( documento )
    
    plantilla = loader.get_template("buscador.html")
    documento = plantilla.render( contexto )
    return HttpResponse( documento )
