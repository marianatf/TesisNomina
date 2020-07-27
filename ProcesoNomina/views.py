from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone
from .models import *
from .render import Render
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required






class Pdf(View):

    def get(self, request, pk):
        sales = Prenomina.objects.filter(pk=pk)
        today = Prenomina.objects.filter(pk=pk)[0]
        prueba = Prenomina.objects.get(pk=pk).pagos_empleados.all()
        total_empleados = Prenomina.objects.get(pk=pk).pagos_empleados.all().aggregate(Sum('monto'))['monto__sum']
        params = {
            'today': today,
            'sales': sales,
            'request': request,
            'prenominapago':prueba,
            'total_emp': total_empleados,

        }
        return Render.render('ProcesoNomina/pdfall.html', params)


def PrenominaLista(request):
    obj = Prenomina.objects.all()
    template_name = 'ProcesoNomina/prenomina/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

def PrenominaVer(request, pk):
    obj = Prenomina.objects.get(pk=pk)
    sales = Prenomina.objects.filter(pk=pk)
    today = Prenomina.objects.filter(pk=pk)[0]
    prueba = Prenomina.objects.get(pk=pk).pagos_empleados.all()
    total_empleados = Prenomina.objects.get(pk=pk).pagos_empleados.all().aggregate(Sum('monto'))['monto__sum']
    template_name = 'ProcesoNomina/prenomina/ver.html'
    context = {
        'object': obj,
        'today': today,
        'sales': sales,
        'request': request,
        'prenominapago': prueba,
        'total_emp': total_empleados,
    }
    return render(request, template_name , context)

def PrenominaCrear(request):
    form = PrenominaForm()
    if request.method == 'POST':
        form = PrenominaForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            return redirect("Lista Prenomina")
    template_name = 'ProcesoNomina/prenomina/crear.html'
    context = {
        "form": form,
    }
    return render(request, template_name , context)


def PrenominaEditar(request, pk):
    obj = get_object_or_404(Prenomina, pk=pk)
    form = PrenominaForm(instance=obj)
    if request.method == 'POST':
        form = PrenominaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Prenomina')
    template_name = 'ProcesoNomina/prenomina/editar.html'
    context = {
        "form": form,
        "object":obj
    }
    return render(request, template_name, context)



def PrenominaBorrar(request, pk):
    obj = get_object_or_404(Prenomina, pk=pk)
    template_name = 'ProcesoNomina/prenomina/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Prenomina")
    context = {"object": obj}
    return render(request, template_name, context)

def NominaLista(request):
    obj = Nomina.objects.all()
    template_name = 'ProcesoNomina/nomina/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

def NominaVer(request, pk):
    obj = Nomina.objects.get(pk=pk)
    sales = Prenomina.objects.filter(pk=obj.prenomina)
    today = Prenomina.objects.filter(pk=obj.prenomina)[0]
    prueba = Prenomina.objects.get(pk=obj.prenomina).pagos_empleados.all()
    total_empleados = Prenomina.objects.get(pk=obj.prenomina).pagos_empleados.all().aggregate(Sum('monto'))['monto__sum']
    template_name = 'ProcesoNomina/nomina/ver.html'
    context = {
        'object': obj,
        'today': today,
        'sales': sales,
        'request': request,
        'prenominapago': prueba,
        'total_emp': total_empleados,
    }
    return render(request, template_name , context)

def NominaCrear(request):
    form = NominaForm()
    if request.method == 'POST':
        form = NominaForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            form = NominaForm()
            return redirect("Lista Nomina")
    template_name = 'ProcesoNomina/nomina/crear.html'
    context = {
        "form": form,
    }
    return render(request, template_name , context)
