from django import forms
from .models import AlumnoTarea

class EntregarTareaForm(forms.ModelForm):
    class Meta:
        model = AlumnoTarea
        fields = ['evidencia']
