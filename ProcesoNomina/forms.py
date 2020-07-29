from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import BlogPost
from .models import *
from ConceptoPago.models import *

class PrenominaForm(forms.ModelForm):
    pagos_empleados = forms.ModelMultipleChoiceField(queryset=PagoEmpleado.objects.filter(prenomina__nomina__isnull=True))
    class Meta:
        model = Prenomina
        fields = ['tipo','descripcion','pagos_empleados','fecha_inicio','fecha_final']
class NominaForm(forms.ModelForm):
    codigo_prenomina = forms.ModelChoiceField(queryset=Prenomina.objects.all().filter(editar=True))
    class Meta:
        model = Nomina
        fields = ['codigo_prenomina','procesado']
