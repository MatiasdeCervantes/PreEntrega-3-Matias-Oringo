from django.shortcuts import render
from django.http import HttpResponse
from AppLibreria.models import clientes, subgeneros, autor
from AppLibreria.forms import ClientesFormulario, SubgenerosFormulario, AutoresFormulario
# Create your views here.

def inicio(request):

    return render(request, "inicio.html")


def crear_cliente(request):

    if request.method == "POST":
        clientes_formulario = ClientesFormulario(request.POST) # se almacena la info del form
        if clientes_formulario.is_valid():
            clientes_dic = clientes_formulario.cleaned_data #se convierte en diccionario
            cliente_nuevo = cliente(nombre=cliente_dic["nombre"], apellido=cliente_dic["apellido"], email=cliente_dic["email"])
            cliente_nuevo.save()
            return render(request, "inicio.html")
    else:

        clientes_formulario = ClientesFormulario()

    return render(request, "clientes.html", {"formu": clientes_formulario})


def crear_autor(request):

    if request.method == "POST":
        autores_formulario = AutoresFormulario(request.POST) # se almacena la info del form
        if autores_formulario.is_valid():
            autores_dic = autores_formulario.cleaned_data #se convierte en diccionario

            autor_nuevo = autor(nombre=autores_dic ["nombre"])
            autor_nuevo.save()
            return render(request, "inicio.html")
    else:

        autores_formulario = AutoresFormulario()

    return render(request, "autores.html", {"formu": autores_formulario})


def crear_subgenero(request):
    
    if request.method == "POST":
        subgenero_formulario = SubgenerosFormulario(request.POST) # se almacena la info del form
        if subgenero_formulario.is_valid():
            subgenero_dic = subgenero_formulario.cleaned_data #se convierte en diccionario
            subgenero_nuevo = subgenero(nombre=subgenero_dic ["nombre"])
            subgenero_nuevo.save()
            return render(request, "inicio.html")
    else:

        subgenero_formulario = SubgenerosFormulario()

    return render(request, "subgeneros.html", {"formu": subgenero_formulario})

def ver_autores(request):

    return render(request, "ver_autores.html")

def ver_clientes(request):

    return render(request, "ver_clientes.html")

def ver_subgeneros(request):

    return render(request, "ver_subgeneros.html")

def buscar_cliente(request):

    if request.GET:
        nombre = request.GET["nombre"]
        cliente = clientes.objects.filter(nombre__icontains=nombre)

        mensaje = f"Buscando cliente {nombre}"

        return render(request, "buscar_cliente.html", {"mensaje":mensaje, "resultado":cliente})

    return render(request, "buscar_cliente.html")

def buscar_autor(request):

    if request.GET:
        nombre = request.GET["nombre"]
        autor_busqueda = autor.objects.filter(nombre__icontains=nombre)

        mensaje = f"Buscando autor {nombre}"

        return render(request, "buscar_autor.html", {"mensaje":mensaje, "resultado":autor_busqueda})

    return render(request, "buscar_autor.html")

def buscar_subgenero(request):

    if request.GET:
        subgenero = request.GET["subgenero"]
        subgenero_busqueda = subgeneros.objects.filter(subgenero__icontains=subgenero)

        mensaje = f"Buscando subgenero {subgenero}"

        return render(request, "buscar_subgenero.html", {"mensaje":mensaje, "resultado":subgenero_busqueda})

    return render(request, "buscar_subgenero.html")

    