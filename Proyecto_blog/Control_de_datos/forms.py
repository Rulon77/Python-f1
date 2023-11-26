from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Pilotos
class EscuderiaFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    nacionalidad = forms.CharField(max_length=256)
    
class PilotoFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    nacionalidad = forms.CharField(label='Nacionalidad')
    biografia = forms.CharField(widget=CKEditorWidget())


