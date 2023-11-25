from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required


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

@login_required
def crear_escuderia(request):
    if request.method == "POST":
       
        formulario = EscuderiaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  
            nombre = data["nombre"]
            nacionalidad = data["nacionalidad"]
          
            escuderia = Escuderias(nombre=nombre, nacionalidad=nacionalidad)
        
            escuderia.save()
            
            url_exitosa = reverse('lista_escuderias')
            return redirect(url_exitosa)
    else:  
        formulario = EscuderiaFormulario()
    
    http_response = render(
        request=request,
        template_name='formulario_escuderia.html',
        context={'formulario': formulario}
    )
    return http_response

@login_required
def crear_piloto(request):
    if request.method == "POST":
        # Form data submission
        formulario = PilotoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # It's a dictionary
            nombre = data["nombre"]
            apellido = data["apellido"]
            nacionalidad = data["nacionalidad"]
            biografia = request.POST.get('biografia', '')
        

            # Create a "Pilotos" object in memory
            piloto = Pilotos(nombre=nombre, apellido=apellido, nacionalidad=nacionalidad, biografia=biografia,)
            
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
        template_name='formulario_piloto_a_mano.html',
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

@login_required    
def eliminar_escuderia(request, id):
    # obtienes el curso de la base de datos
    escuderia = Escuderias.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        escuderia.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('lista_escuderias')
        return redirect(url_exitosa)    

@login_required
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

@login_required
def editar_piloto(request, id):
    piloto = Pilotos.objects.get(id=id)
    if request.method == "POST":
        # Actualizacion de datos
        formulario = PilotoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            piloto.nombre = data['nombre']
            piloto.apellido = data['apellido']
            piloto.nacionalidad = data['nacionalidad']
            piloto.biografia = data['biografia']
            
            piloto.save()

            url_exitosa = reverse('lista_pilotos')
            return redirect(url_exitosa)
    else:  
        inicial = {
            'nombre': piloto.nombre,
            'apellido': piloto.apellido,
            'nacionalidad': piloto.nacionalidad,
            'biografia': piloto.biografia,
        }
        formulario = PilotoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='formulario_piloto.html',
        context={'formulario': formulario},
    )

@login_required    
def eliminar_piloto(request, id):
    # obtienes el curso de la base de datos
    piloto = Pilotos.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        piloto.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('lista_pilotos')
        return redirect(url_exitosa)  

def buscar_pilotos(request):


    if (request.method == "POST"):
        data = request.POST
        busqueda = data["busqueda"]
        busqueda_piloto = Pilotos.objects.filter(
            Q(nacionalidad__icontains=busqueda) | Q(nombre__contains=busqueda) | Q(apellido__contains=busqueda)
        )
        contexto = {"pilotos": busqueda_piloto,}
        
        http_response = render(
            request=request,
            template_name='lista_pilotos.html',
            context=contexto,
        )
        return http_response    
       
       
def detalle_piloto(request, piloto_id):
    piloto = get_object_or_404(Pilotos, pk=piloto_id)
    return render(request, 'detalle_piloto.html', {'piloto': piloto})       