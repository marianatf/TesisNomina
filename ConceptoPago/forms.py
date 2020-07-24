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
        fields = ['descripcion','codigo_ad','codigo_formula','frecuencia','codigo_fv','empleado_pago']

class PagoEmpleadoForm(forms.ModelForm):
    class Meta:
        model = PagoEmpleado
        fields = ['codigo_pago','codigo_empleado','elemento_pago','cantidad','monto','formula']