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

def home(request):
    context = {
    }
    return render(request, 'RecursosHumanos/home.html', context)


def PersonaLista(request):
    obj = Persona.objects.all()
    template_name = 'RecursosHumanos/persona/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)


def PersonaCrear(request):
    form = PersonaForm()
    if request.method == 'POST':
        form = PersonaForm(request.POST)
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


def PersonaEditar(request, pk):
    obj = get_object_or_404(Persona, pk=pk)
    form = PersonaForm(instance=obj)
    if request.method == 'POST':
        PersonaForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Candidato')
        else:
            raise Http404
    template_name = 'RecursosHumanos/persona/editar.html'
    context = {
        "form": form,
        "object":obj
    }
    return render(request, template_name, context)

def PersonaVer(request, pk):
    obj = Persona.objects.get(pk=pk)
    template_name = 'RecursosHumanos/persona/ver.html'
    context = {
        'object': obj
    }
    return render(request, template_name , context)

def PersonaBorrar(request, pk):
    obj = get_object_or_404(Persona, pk=pk)
    template_name = 'RecursosHumanos/persona/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Candidato")
    context = {"object": obj}
    return render(request, template_name, context)


def EscalaLista(request):
    obj = Escala.objects.all()
    template_name = 'RecursosHumanos/escala/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)


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


def EscalaEditar(request, pk):
    obj = get_object_or_404(Escala, pk=pk)
    form = EscalaForm(instance=obj)
    if request.method == 'POST':
        EscalaForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Escala')
        else:
            raise Http404
    template_name = 'RecursosHumanos/escala/editar.html'
    context = {
        "form": form,
        "object": obj
    }
    return render(request, template_name, context)

def EscalaBorrar(request, pk):
    obj = get_object_or_404(Escala, pk=pk)
    template_name = 'RecursosHumanos/escala/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Escala")
    context = {"object": obj}
    return render(request, template_name, context)

def DepartamentoLista(request):
    obj = Departamento.objects.all()
    template_name = 'RecursosHumanos/departamento/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)


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


def DepartamentoEditar(request, pk):
    obj = get_object_or_404(Departamento, pk=pk)
    form = DepartamentoForm(instance=obj)
    if request.method == 'POST':
        DepartamentoForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Departamento')
        else:
            raise Http404
    template_name = 'RecursosHumanos/departamento/editar.html'
    context = {
        "form": form,
        "object": obj
    }
    return render(request, template_name, context)

def DepartamentoBorrar(request, pk):
    obj = get_object_or_404(Departamento, pk=pk)
    template_name = 'RecursosHumanos/departamento/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Departamento")
    context = {"object": obj}
    return render(request, template_name, context)

def CargoLista(request):
    obj = Cargo.objects.all()
    template_name = 'RecursosHumanos/cargo/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)


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


def CargoEditar(request, pk):
    obj = get_object_or_404(Cargo, pk=pk)
    form = CargoForm(instance=obj)
    if request.method == 'POST':
        CargoForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Cargo')
        else:
            raise Http404
    template_name = 'RecursosHumanos/cargo/editar.html'
    context = {
        "form": form,
        "object": obj
    }
    return render(request, template_name, context)

def CargoBorrar(request, pk):
    obj = get_object_or_404(Cargo, pk=pk)
    template_name = 'RecursosHumanos/cargo/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Cargo")
    context = {"object": obj}
    return render(request, template_name, context)

def RacLista(request):
    obj = Rac.objects.all()
    template_name = 'RecursosHumanos/rac/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)

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


def RacEditar(request, pk):
    obj = get_object_or_404(Rac, pk=pk)
    form = RacForm(instance=obj)
    if request.method == 'POST':
        RacForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Rac')
        else:
            raise Http404
    template_name = 'RecursosHumanos/rac/editar.html'
    context = {
        "form": form,
        "object": obj
    }
    return render(request, template_name, context)

def RacBorrar(request, pk):
    obj = get_object_or_404(Rac, pk=pk)
    template_name = 'RecursosHumanos/rac/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Rac")
    context = {"object": obj}
    return render(request, template_name, context)

def EmpleadoLista(request):
    obj = Empleado.objects.all()
    template_name = 'RecursosHumanos/empleado/lista.html'
    context = {
        'objects': obj
    }
    return render(request, template_name , context)


def EmpleadoCrear(request):
    form = EmpleadoForm()
    if request.method == 'POST':
        form = EmpleadoForm(request.POST or None)
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


def EmpleadoEditar(request, pk):
    obj = get_object_or_404(Empleado, pk=pk)
    form = EmpleadoForm(instance=obj)
    if request.method == 'POST':
        EmpleadoForm(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('Lista Empleado')
        else:
            raise Http404
    template_name = 'RecursosHumanos/empleado/editar.html'
    context = {
        "form": form,
        "object": obj
    }
    return render(request, template_name, context)

def EmpleadoVer(request, pk):
    obj = Empleado.objects.get(pk=pk)
    template_name = 'RecursosHumanos/empleado/ver.html'
    context = {
        'object': obj
    }
    return render(request, template_name , context)

def EmpleadoBorrar(request, pk):
    obj = get_object_or_404(Empleado, pk=pk)
    template_name = 'RecursosHumanos/empleado/borrar.html'
    if request.method == "POST":
        obj.delete()
        return redirect("Lista Empleado")
    context = {"object": obj}
    return render(request, template_name, context)

# def LoginPage(request):
#     form = IngresoEmpresaForm()
#     if request.method =='POST':
#         usernames = request.POST['username']
#         passwords = request.POST['password']
#
#         user = authenticate(request, username=usernames, password=passwords)
#         if user is not None:
#             login(request, user)
#             return redirect('/system/%s/dashboard' %(form.empresa))
#         else:
#             messages.info(request, 'Username or Password is Wrong')
#     context = {
#         'empresas':obj
#     }
#     return render(request, 'accounts/login.html',context)