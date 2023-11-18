from django.urls import path

from . import views

# Son las URLS de la app control_estudios
urlpatterns = [
    path('pilotos/', views.lista_pilotos, name='lista_pilotos'),
    path("escuderias/", views.lista_Escuderias, name="lista_escuderias"),
    path("calendario/", views.lista_Calendario, name="calendario"),
    path("buscarescuderias/", views.buscar_escuderias, name="buscar_escuderias"),
    path("crear_escuderia/", views.crear_escuderia, name="crear_escuderia"),
    path("crear_piloto/", views.crear_piloto, name="crear_piloto"),
    path("eliminar-escuderia/<int:id>/", views.eliminar_escuderia, name="eliminar_escuderia"),
    path("editar-escuderia/<int:id>/", views.editar_escuderia, name="editar_escuderia"),

]
