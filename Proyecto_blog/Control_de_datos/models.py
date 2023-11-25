from django.db import models

# Create your models here.
class Escuderias(models.Model):
    # los atributos de clase (son las columnas de la tabla)
    nombre = models.CharField(max_length=64)
    nacionalidad = models.CharField(max_length=256)
    
    def __str__(self):
        return f"{self.nombre} ({self.nacionalidad})"


class Pilotos(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    nacionalidad = models.CharField(max_length=256)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Calendario(models.Model):
    nombre = models.CharField(max_length=256)
    pais = models.CharField(max_length=256)
    fecha = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.pais}, {self.fecha}"        

class Meta:
    app_label = 'Control_de_datos'    