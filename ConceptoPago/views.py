from .forms import *
from .models import *
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

def VariableLista(request):
    obj = Variable.objects.all()
    template_name = 'ConceptoPago/variable/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

def VariableCrear(request):
    form = VariableForm()
    if request.method == 'POST':
        form = VariableForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            form = VariableForm()
            return redirect("Lista Variable")
    template_name = 'ConceptoPago/variable/crear.html'
    context = {
        "form": form
    }
    return render(request, template_name , context)

def VariableEditar(request, pk):
    obj = get_object_or_404(Variable, pk=pk)
    form = VariableForm(instance=obj)
    if request.method == 'POST':
        form = VariableForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Variable')
    template_name = 'ConceptoPago/variable/editar.html'
    context = {
        "form": form,
        "object":obj
    }
    return render(request, template_name, context)


def VariableBorrar(request, pk):
    obj = get_object_or_404(Variable, pk=pk)
    template_name = 'ConceptoPago/variable/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Variable")
    context = {"object": obj}
    return render(request, template_name, context)



def FormulacionLista(request):
    obj = Formulacion.objects.all()
    template_name = 'ConceptoPago/formulacion/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

def FormulacionCrear(request):
    form = FormulacionForm()
    obj = Variable.objects.all()
    if request.method == 'POST':
        form = FormulacionForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            form = FormulacionForm()
            return redirect("Lista Formulacion")
    template_name = 'ConceptoPago/formulacion/crear.html'
    context = {
        "form": form,
        "object_list_2":obj
    }
    return render(request, template_name , context)

def FormulacionEditar(request, pk):
    obj = get_object_or_404(Formulacion, pk=pk)
    obj2 = Variable.objects.all()
    form = FormulacionForm(instance=obj)
    if request.method == 'POST':
        form = FormulacionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Formulacion')
    template_name = 'ConceptoPago/formulacion/editar.html'
    context = {
        "form": form,
        "object":obj,
        "object_list_2": obj2
    }
    return render(request, template_name, context)



def FormulacionBorrar(request, pk):
    obj = get_object_or_404(Formulacion, pk=pk)
    template_name = 'ConceptoPago/formulacion/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Formulacion")
    context = {"object": obj}
    return render(request, template_name, context)


def ElementoPagoLista(request):
    obj = ElementoPago.objects.all()
    template_name = 'ConceptoPago/elementopago/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

def ElementoPagoCrear(request):
    form = ElementoPagoForm()
    obj = Variable.objects.all()
    if request.method == 'POST':
        form = ElementoPagoForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            form = ElementoPagoForm()
            return redirect("Lista ElementoPago")
    template_name = 'ConceptoPago/elementopago/crear.html'
    context = {
        "form": form,
        "object_list_2":obj
    }
    return render(request, template_name , context)

def ElementoPagoEditar(request, pk):
    obj = get_object_or_404(ElementoPago, pk=pk)
    form = ElementoPagoForm(instance=obj)
    if request.method == 'POST':
        form = ElementoPagoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista ElementoPago')
    template_name = 'ConceptoPago/elementopago/editar.html'
    context = {
        "form": form,
        "object":obj
    }
    return render(request, template_name, context)



def ElementoPagoBorrar(request, pk):
    obj = get_object_or_404(ElementoPago, pk=pk)
    template_name = 'ConceptoPago/elementopago/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista ElementoPago")
    context = {"object": obj}
    return render(request, template_name, context)


def PagoEmpleadoLista(request):
    obj = PagoEmpleado.objects.all()
    template_name = 'ConceptoPago/pagoempleado/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

def PagoEmpleadoCrear(request):
    form = PagoEmpleadoForm()
    if request.method == 'POST':
        form = PagoEmpleadoForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user
            obj.save()
            form = PagoEmpleadoForm()
            return redirect("Lista PagoEmpleado")
    template_name = 'ConceptoPago/pagoempleado/crear.html'
    context = {
        "form": form,
    }
    return render(request, template_name , context)


def PagoEmpleadoEditar(request, pk):
    obj = get_object_or_404(PagoEmpleado, pk=pk)
    form = PagoEmpleadoForm(instance=obj)
    if request.method == 'POST':
        form = PagoEmpleadoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista PagoEmpleado')
    template_name = 'ConceptoPago/pagoempleado/editar.html'
    context = {
        "form": form,
        "object":obj
    }
    return render(request, template_name, context)


def PagoEmpleadoBorrar(request, pk):
    obj = get_object_or_404(PagoEmpleado, pk=pk)
    template_name = 'ConceptoPago/pagoempleado/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista PagoEmpleado")
    context = {"object": obj}
    return render(request, template_name, context)