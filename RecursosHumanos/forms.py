from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import BlogPost
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import inlineformset_factory

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre','rif','fecha_creacion','ceo','cantidad_empleado','proposito',]

class IngresoEmpresaForm(forms.Form):
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), empty_label="Empresas")

class PersonaForm(forms.ModelForm):
    cargo_optar = forms.ModelChoiceField(queryset=Cargo.objects.all())
    class Meta:
        model = Persona
        fields = ['codigo_solicitud', 'status', 'cedula', 'apellido', 'nombre', 'segundo_nombre', 'segundo_apellido', 'fecha_nacimiento', 'ocupacion_actual', 'cargo_optar', 'email', 'telefono', 'genero', 'imagen', 'direccion','rif','nacionalidad','municipio','parroquia','estado','profesion']


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
        fields = ['codigo_departamento', 'codigo_cargo', 'codigo_escala']

class EmpleadoForm(forms.ModelForm):
    codigo_rac = forms.ModelChoiceField(queryset=Rac.objects.all().filter(cargo_ocupado=False))
    class Meta:
        model = Empleado
        fields = ['cedula', 'codigo_solicitud', 'apellido', 'nombre', 'segundo_apellido', 'segundo_nombre', 'codigo_solicitud', 'codigo_rac', 'sueldo', 'fecha_nacimiento', 'email', 'telefono', 'genero', 'imagen', 'status_trabajador', 'direccion','fecha_ingreso', 'profesion', 'estado', 'municipio', 'parroquia', 'nacionalidad', 'rif', 'estado_civil', 'forma_pago', 'tipo_cuenta', 'banco', 'cuenta']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['codigo_solicitud'].widget.attrs['onchange'] = "load_email()"

class FamiliaEmpleadoForm(forms.ModelForm):
    class Meta:
        model = FamiliaEmpleado
        exclude = ()
FamiliaEmpleadoFormSet = inlineformset_factory(Empleado, FamiliaEmpleado, form=FamiliaEmpleadoForm, extra=2, max_num=5)

class EducacionEmpleadoForm(forms.ModelForm):
    class Meta:
        model = EducacionEmpleado
        exclude = ()
EducacionEmpleadoFormSet = inlineformset_factory(Empleado, EducacionEmpleado, form=EducacionEmpleadoForm, extra=1, max_num=3)

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