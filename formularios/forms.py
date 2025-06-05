from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm): #defines una clae de formulario. crea un formulario automaticamente con los campos que yo te diga sacados de modelo "Formulario"
    class Meta:
        model = Formulario
        fields = [
            'nombre_proyecto',
            'descripcion',
            'cantidad_trabajadores',
            'peso_residuo',
            'fecha_inicio',
            'tipo_residuo',
            'es_peligroso',
            'documento',
            'completo'
        ]

#no estamos incluyendo ni usuario ni grupo, esta bien, porque se rellenan directamente en la vista (formulario.usuario= request.user)
