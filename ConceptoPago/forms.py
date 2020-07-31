from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import BlogPost
from .models import *

class VariableForm(forms.ModelForm):
    class Meta:
        model = Variable
        fields = ['descripcion','monto']
class FormulacionForm(forms.ModelForm):
    class Meta:
        model = Formulacion
        fields = ['descripcion','formula']


class ElementoPagoForm(forms.ModelForm):
    class Meta:
        model = ElementoPago
        fields = ['descripcion','codigo_ad','codigo_formula','empleado_pago']

class PagoEmpleadoForm(forms.ModelForm):
    elemento_pago = forms.ModelChoiceField(queryset=ElementoPago.objects.filter(pagoempleado__prenomina__nomina__isnull=True))
    class Meta:
        model = PagoEmpleado
        fields = ['codigo_pago','codigo_empleado','elemento_pago','cantidad','monto','formula']