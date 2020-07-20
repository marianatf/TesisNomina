from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import BlogPost
from .models import *


class PrenominaForm(forms.ModelForm):
    class Meta:
        model = Prenomina
        fields = ['tipo','descripcion','pagos_empleados','fecha_inicio','fecha_final']
class NominaForm(forms.ModelForm):
    class Meta:
        model = Nomina
        fields = ['codigo_prenomina','procesado']
    class Media:
        css = {'all': ['admin/css/widgets.css']}
        js = ['/admin/jsi18n/']
