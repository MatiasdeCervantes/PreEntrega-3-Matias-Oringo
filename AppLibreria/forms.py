from django import forms

class AutoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)

class SubgenerosFormulario(forms.Form):
    subgenero = forms.CharField(max_length=15)
    editorial = forms.CharField(max_length=30)

class ClientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)