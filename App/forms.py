from django import forms
from .models import Tarea


class FormTarea(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo','descripcion','importante']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe el titulo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe la descripcion'}),
            'importante': forms.CheckboxInput(attrs={'class': 'form-check-input m-5'})
        }