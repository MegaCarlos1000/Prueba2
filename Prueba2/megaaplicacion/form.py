from django import forms
from megaaplicacion.models import Proyecto

class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields ="__all__"