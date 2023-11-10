from django import forms
class EscuderiaFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    nacionalidad = forms.CharField(max_length=256)
    
class PilotoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=64)
    nacionalidad = forms.CharField(max_length=256)    
