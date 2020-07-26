from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import BlogPost
from .models import *
from django.contrib.admin.widgets import AdminDateWidget

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre','rif','fecha_creacion','ceo','cantidad_empleado','proposito',]

class IngresoEmpresaForm(forms.Form):
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), empty_label="Empresas")

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['codigo_solicitud', 'status', 'cedula', 'apellido', 'nombre', 'segundo_nombre', 'segundo_apellido', 'fecha_nacimiento', 'edad', 'ocupacion_actual', 'cargo_optar', 'email', 'telefono', 'genero', 'imagen', 'direccion']


class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = ['nombre','apellido']


class EscalaForm(forms.ModelForm):
    class Meta:
        model = Escala
        fields = ['escala', 'grado', 'paso', 'sueldo']

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['descripcion', 'cantidad_empleado', 'presupuesto']

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['cargo', 'descripcion']

class RacForm(forms.ModelForm):
    class Meta:
        model = Rac
        fields = ['codigo_departamento', 'codigo_cargo', 'codigo_escala', 'compensacion', 'cargo_ocupado']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['cedula', 'codigo_solicitud', 'apellido', 'nombre', 'segundo_apellido', 'segundo_nombre', 'codigo_solicitud', 'codigo_rac', 'sueldo', 'fecha_nacimiento', 'edad', 'email', 'telefono', 'genero', 'imagen', 'status_trabajador', 'direccion','fecha_ingreso']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['codigo_solicitud'].widget.attrs['onchange'] = "load_email()"


# class BlogPostForm(forms.Form):
#     title = forms.CharField()
#     slug = forms.SlugField()
#     content = forms.CharField(widget=forms.Textarea)
# class BlogPostModelForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['title', 'image', 'slug', 'content', 'publish_date']
#
#     def clean_title(self, *args, **kwargs):
#         instance = self.instance
#         title = self.cleaned_data.get('title')
#         qs = BlogPost.objects.filter(title__iexact=title)
#         if instance is not None:
#             qs = qs.exclude(pk=instance.pk) # id=instance.id
#         if qs.exists():
#             raise forms.ValidationError("This title has already been used. Please try again.")
#         return title