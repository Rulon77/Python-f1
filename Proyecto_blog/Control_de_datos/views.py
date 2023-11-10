from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from .forms import *
from .models import *


def lista_pilotos(request):
    pilotos = Pilotos.objects.all()
    return render(request, 'lista_pilotos.html', {'pilotos': pilotos})

def lista_Escuderias(request):
    escuderias = Escuderias.objects.all()
    return render(request, 'lista_escuderias.html', {'escuderias': escuderias})

def lista_Calendario(request):
    calendario = Calendario.objects.all()
    return render(request, 'lista_calendario.html', {'calendario': calendario})

def crear_escuderia(request):
    if request.method == "POST":
        # Form data submission
        formulario = EscuderiaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # It's a dictionary
            nombre = data["nombre"]
            nacionalidad = data["nacionalidad"]

            # Create a "Pilotos" object in memory
            escuderia = Escuderias(nombre=nombre, nacionalidad=nacionalidad)
            
            # Save the object to the database
            escuderia.save()

            # Redirect the user to the list of "Pilotos"
            url_exitosa = reverse('lista_escuderias')
            return redirect(url_exitosa)
    else:  # GET request
        # Render the initial form
        formulario = EscuderiaFormulario()
    
    http_response = render(
        request=request,
        template_name='formulario_escuderia.html',
        context={'formulario': formulario}
    )
    return http_response

def crear_piloto(request):
    if request.method == "POST":
        # Form data submission
        formulario = PilotoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # It's a dictionary
            nombre = data["nombre"]
            apellido = data["apellido"]
            nacionalidad = data["nacionalidad"]
        

            # Create a "Pilotos" object in memory
            piloto = Pilotos(nombre=nombre, apellido=apellido, nacionalidad=nacionalidad,)
            
            # Save the object to the database
            piloto.save()

            # Redirect the user to the list of "Pilotos"
            url_exitosa = reverse('lista_pilotos')
            return redirect(url_exitosa)
    else:  # GET request
        # Render the initial form
        formulario = PilotoFormulario()
    
    http_response = render(
        request=request,
        template_name='formulario_piloto.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_escuderias(request):
    if (request.method == "POST"):
        data = request.POST
        busqueda = data["busqueda"]
        busqueda_escuderia = Escuderias.objects.filter(
            Q(nacionalidad__icontains=busqueda) | Q(nombre__contains=busqueda)
        )
        contexto = {"escuderias": busqueda_escuderia,}
        
        http_response = render(
            request=request,
            template_name='lista_escuderias.html',
            context=contexto,
        )
        return http_response
    

    