from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import BlogPost
#

from .models import *


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre','rif','fecha_creacion','ceo','cantidad_empleado','proposito',]

class IngresoEmpresaForm(forms.Form):
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), empty_label="Empresas")



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