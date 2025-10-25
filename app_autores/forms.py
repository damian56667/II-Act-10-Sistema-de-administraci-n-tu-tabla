from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['autor_id', 'nombre', 'apellido', 'nacionalidad', 'fecha_nacimiento', 'bibliografia', 'pagina_web']
        widgets = {
            'autor_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bibliografia': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'pagina_web': forms.URLInput(attrs={'class': 'form-control'}),
        }
