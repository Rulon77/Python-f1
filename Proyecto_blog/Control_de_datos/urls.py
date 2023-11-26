from django.urls import path

from . import views


urlpatterns = [
    path('pilotos/', views.lista_pilotos, name='lista_pilotos'),
    path("escuderias/", views.lista_Escuderias, name="lista_escuderias"),
    path("calendario/", views.lista_Calendario, name="calendario"),
    path('sobre_mi/', views.sobre_mi, name='sobre_mi'),
    
    
    #Escuderia
    path("crear_escuderia/", views.crear_escuderia, name="crear_escuderia"),
    path("editar_escuderia/<int:id>/", views.editar_escuderia, name="editar_escuderia"),
    path("eliminar_escuderia/<int:id>/", views.eliminar_escuderia, name="eliminar_escuderia"),
    path("buscar_escuderias/", views.buscar_escuderias, name="buscar_escuderias"),
    
    #Pilotos
    path("crear_piloto/", views.crear_piloto, name="crear_piloto"),
    path('detalle_piloto/<int:piloto_id>/', views.detalle_piloto, name='detalle_piloto'),
    path("editar_piloto/<int:id>/", views.editar_piloto, name="editar_piloto"),
    path("eliminar_piloto/<int:id>/", views.eliminar_piloto, name="eliminar_piloto"),
    path("buscar_piloto/", views.buscar_pilotos, name="buscar_piloto"),
    
    
]
