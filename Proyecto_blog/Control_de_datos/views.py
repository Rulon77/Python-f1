from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
    
def eliminar_escuderia(request, id):
    # obtienes el curso de la base de datos
    escuderia = Escuderias.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        escuderia.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('lista_escuderias')
        return redirect(url_exitosa)    

def editar_escuderia(request, id):
    escuderia = Escuderias.objects.get(id=id)
    if request.method == "POST":
        # Actualizacion de datos
        formulario = EscuderiaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            # modificamos el objeto en memoria RAM
            escuderia.nombre = data['nombre']
            escuderia.nacionalidad = data['nacionalidad']
            # Los cambios se guardan en la Base de datos
            escuderia.save()

            url_exitosa = reverse('lista_escuderias')
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario con data actual
        inicial = {
            'nombre': escuderia.nombre,
            'nacionalidad': escuderia.nacionalidad,
        }
        formulario = EscuderiaFormulario(initial=inicial)
    return render(
        request=request,
        template_name='formulario_escuderia.html',
        context={'formulario': formulario},
    )
    