from django import forms
from .models import AlumnoTarea
from .models import Duda
class EntregarTareaForm(forms.ModelForm):
    class Meta:
        model = AlumnoTarea
        fields = ['evidencia']

class DudaForm(forms.ModelForm):
    class Meta:
        model = Duda
        fields = ['asunto', 'descripcion']
        widgets = {
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows':10}),
        }