from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from ProcesoNomina.models import *
from django.db.models import Sum
from django.forms import modelformset_factory, inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from ConceptoPago.models import *
from ProcesoNomina.models import *


@unauthenticated_user
def LoginPage(request):
    if request.method =='POST':
        usernames = request.POST['username']
        passwords = request.POST['password']
        user = authenticate(request, username=usernames, password=passwords)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('Dashboard')
        else:
            messages.info(request, 'Usuario o Clave Erroneo')
    context = {}
    return render(request, 'RecursosHumanos/login.html',context)

def LogoutUser(request):
    logout(request)
    return redirect('Login')

@login_required(login_url='Login')
def myview(request):
    form = EmpleadoForm(request.POST)
    if form.is_valid():
        db = form.save(commit=False)
        db.email = Persona.objects.get(id__exact=form['codigo_solicitud'].value()).email
        form = EmpleadoForm(instance=db)
        content = {'form': form}
        return render(request, 'RecursosHumanos/empleados/crear.html', content)
    else:
        content = {'form': form}
        return render(request, 'RecursosHumanos/empleados/crear.html', content)


@login_required(login_url='Login')
def home(request):
    solicitud = Persona.objects.all().filter(empleado__isnull=True).count()
    empleados = Empleado.objects.all().count()
    cargo = Cargo.objects.all().count()
    rac = Rac.objects.all().filter(cargo_ocupado=False).count()
    empresa = get_object_or_404(Empresa, pk=1)
    total_empleados = Nomina.objects.all().prefetch_related('codigo_prenomina__pagos_empleados').aggregate(Sum('codigo_prenomina__pagos_empleados__monto'))['codigo_prenomina__pagos_empleados__monto__sum']
    nomina = Nomina.objects.all().count()

    context = {
        'objectpersona':solicitud,
        'objectempleados': empleados,
        'objectrac':rac,
        'objectcargo':cargo,
        'object':empresa,
        'total':total_empleados,
        'total_n':nomina

    }
    return render(request, 'RecursosHumanos/home.html', context)

@login_required(login_url='Login')
def PersonaLista(request):
    obj = Persona.objects.all().filter(empleado__isnull=True)
    template_name = 'RecursosHumanos/persona/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def PersonaCrear(request):
    form = PersonaForm()
    if request.method == 'POST':
        form = PersonaForm(request.POST,request.FILES or None)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            form = PersonaForm()
            return redirect("/candidato")
        else:
            messages.info(request, 'Username or Password is Wrong')


    template_name = 'RecursosHumanos/persona/crear.html'
    context = {
        "form": form
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def PersonaEditar(request, pk):
    obj = get_object_or_404(Persona, pk=pk)
    form = PersonaForm(instance=obj)
    if request.method == 'POST':
        form = PersonaForm(request.POST, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Candidato')
    template_name = 'RecursosHumanos/persona/editar.html'
    context = {
        "form": form,
        "object":obj
    }
    return render(request, template_name, context)


@login_required(login_url='Login')
def PersonaVer(request, pk):
    obj = Persona.objects.get(pk=pk)
    template_name = 'RecursosHumanos/persona/ver.html'
    context = {
        'object': obj
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def PersonaBorrar(request, pk):
    obj = get_object_or_404(Persona, pk=pk)
    template_name = 'RecursosHumanos/persona/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Candidato")
    context = {"object": obj}
    return render(request, template_name, context)

@login_required(login_url='Login')
def PersonaAgregar(request, pk):
    obj = get_object_or_404(Persona, pk=pk)
    template_name = 'RecursosHumanos/persona/familia.html'
    FamiliaFormset = inlineformset_factory(Persona, Familia, form=FamiliaForm, extra=1)
    # if request.method == "POST":
    #     formset = FamiliaFormset(request.POST, queryset=Familia.objects.filter(persona__codigo_solicitud=obj.pk))
        #return redirect("Lista Candidato")
    formset = FamiliaFormset(request.POST, queryset=Familia.objects.filter(persona__codigo_solicitud=obj.pk))
    context = {"object": obj,
               "formset":formset}
    return render(request, template_name, context)

@login_required(login_url='Login')
def EscalaLista(request):
    obj = Escala.objects.all()
    template_name = 'RecursosHumanos/escala/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def EscalaCrear(request):
    form = EscalaForm()
    if request.method == 'POST':
        form = EscalaForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            return redirect("Lista Escala")
    template_name = 'RecursosHumanos/escala/crear.html'
    context = {
        "form": form
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def EscalaEditar(request, pk):
    obj = get_object_or_404(Escala, pk=pk)
    form = EscalaForm(instance=obj)
    if request.method == 'POST':
        form = EscalaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Escala')
    template_name = 'RecursosHumanos/escala/editar.html'
    context = {
        "form": form,
        "object":obj
    }
    return render(request, template_name, context)

@login_required(login_url='Login')
def EscalaBorrar(request, pk):
    obj = get_object_or_404(Escala, pk=pk)
    template_name = 'RecursosHumanos/escala/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Escala")
    context = {"object": obj}
    return render(request, template_name, context)

@login_required(login_url='Login')
def DepartamentoLista(request):
    obj = Departamento.objects.all()
    template_name = 'RecursosHumanos/departamento/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def DepartamentoCrear(request):
    form = DepartamentoForm()
    if request.method == 'POST':
        form = DepartamentoForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            return redirect("Lista Departamento")
    template_name = 'RecursosHumanos/departamento/crear.html'
    context = {
        "form": form
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def DepartamentoEditar(request, pk):
    obj = get_object_or_404(Departamento, pk=pk)
    form = DepartamentoForm(instance=obj)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Departamento')
    template_name = 'RecursosHumanos/departamento/editar.html'
    context = {
        "form": form,
        "object":obj
    }
    return render(request, template_name, context)

@login_required(login_url='Login')
def DepartamentoBorrar(request, pk):
    obj = get_object_or_404(Departamento, pk=pk)
    template_name = 'RecursosHumanos/departamento/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Departamento")
    context = {"object": obj}
    return render(request, template_name, context)


@login_required(login_url='Login')
def CargoLista(request):
    obj = Cargo.objects.all()
    template_name = 'RecursosHumanos/cargo/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def CargoCrear(request):
    form = CargoForm()
    if request.method == 'POST':
        form = CargoForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            return redirect("Lista Cargo")
    template_name = 'RecursosHumanos/cargo/crear.html'
    context = {
        "form": form
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def CargoEditar(request, pk):
    obj = get_object_or_404(Cargo, pk=pk)
    form = CargoForm(instance=obj)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Cargo')
    template_name = 'RecursosHumanos/cargo/editar.html'
    context = {
        "form": form,
        "object":obj
    }
    return render(request, template_name, context)

@login_required(login_url='Login')
def CargoBorrar(request, pk):
    obj = get_object_or_404(Cargo, pk=pk)
    template_name = 'RecursosHumanos/cargo/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Cargo")
    context = {"object": obj}
    return render(request, template_name, context)

@login_required(login_url='Login')
def RacLista(request):
    obj = Rac.objects.all()
    template_name = 'RecursosHumanos/rac/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def RacCrear(request):
    form = RacForm()
    if request.method == 'POST':
        form = RacForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            return redirect("Lista Rac")
    template_name = 'RecursosHumanos/rac/crear.html'
    context = {
        "form": form
    }
    return render(request, template_name , context)


@login_required(login_url='Login')
def RacEditar(request, pk):
    obj = get_object_or_404(Rac, pk=pk)
    form = RacForm(instance=obj)
    if request.method == 'POST':
        form = RacForm(request.POST, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Rac')
    template_name = 'RecursosHumanos/rac/editar.html'
    context = {
        "form": form,
        "object":obj
    }
    return render(request, template_name, context)

@login_required(login_url='Login')
def RacBorrar(request, pk):
    obj = get_object_or_404(Rac, pk=pk)
    template_name = 'RecursosHumanos/rac/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Rac")
    context = {"object": obj}
    return render(request, template_name, context)


@login_required(login_url='Login')
def EmpleadoLista(request):
    obj = Empleado.objects.all()
    template_name = 'RecursosHumanos/empleado/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def EmpleadoCrear(request):
    form = EmpleadoForm()
    if request.method == 'POST':
        form = EmpleadoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            return redirect("Lista Empleado")
    template_name = 'RecursosHumanos/empleado/crear.html'
    context = {
        "form": form
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def EmpleadoEditar(request, pk):
    obj = get_object_or_404(Empleado, pk=pk)
    form = EmpleadoForm(instance=obj)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Empleado')
    template_name = 'RecursosHumanos/empleado/editar.html'
    context = {
        "form": form,
        "object":obj
    }
    return render(request, template_name, context)

@login_required(login_url='Login')
def EmpleadoVer(request, pk):
    obj = Empleado.objects.get(pk=pk)
    empleado_ad = Nomina.objects.get(pk=1).codigo_prenomina.pagos_empleados.filter(codigo_empleado__pk=1)
    total_pagado = Nomina.objects.all().filter(codigo_prenomina__pagos_empleados__codigo_empleado__pk=1).aggregate(Sum('codigo_prenomina__pagos_empleados__monto'))['codigo_prenomina__pagos_empleados__monto__sum']
    template_name = 'RecursosHumanos/empleado/ver.html'
    context = {
        'object': obj
    }
    return render(request, template_name , context)

@login_required(login_url='Login')
def EmpleadoBorrar(request, pk):
    obj = get_object_or_404(Empleado, pk=pk)
    template_name = 'RecursosHumanos/empleado/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Empleado")
    context = {"object": obj}
    return render(request, template_name, context)


def FamiliaEmpleadoVer(request, pk):
    obj = Empleado.objects.get(pk=pk)
    formset = FamiliaEmpleadoFormSet(request.POST or None, instance=obj)
    if formset.is_valid():
        formset.save()
        return redirect('Lista Empleado')
    template_name = 'RecursosHumanos/familiaempleado/ver.html'
    context = {
        "formset":formset
    }
    return render(request, template_name, context)

def EducacionEmpleadoVer(request, pk):
    obj = Empleado.objects.get(pk=pk)
    formset = EducacionEmpleadoFormSet(request.POST or None, instance=obj)
    if formset.is_valid():
        formset.save()
        return redirect('Lista Empleado')
    template_name = 'RecursosHumanos/educacionempleado/ver.html'
    context = {
        "formset":formset
    }
    return render(request, template_name, context)