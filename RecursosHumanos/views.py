from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.

def home(request):
    context = {
    }
    return render(request, 'RecursosHumanos/home.html', context)

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