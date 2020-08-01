"""nomina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include # url
from django.conf.urls.static import static
from django.conf import settings
from RecursosHumanos.views import *
from ConceptoPago.views import *
from ProcesoNomina.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='Dashboard'),
    path('login/', LoginPage, name='Login'),
    path('logout/', LogoutUser, name='Logout'),
    path('candidato/', PersonaLista, name='Lista Candidato'),
    path('candidato/crear', PersonaCrear, name='Crear Candidato'),
    path('candidato/editar/<int:pk>', PersonaEditar, name='Editar Candidato'),
    path('candidato/ver/<int:pk>', PersonaVer, name='Ver Candidato'),
    path('candidato/eliminar/<int:pk>', PersonaBorrar, name='Eliminar Candidato'),
    path('candidato/familia/<int:pk>', PersonaAgregar, name='Agregar FamEdu'),

    path('escala/', EscalaLista, name='Lista Escala'),
    path('escala/crear', EscalaCrear, name='Crear Escala'),
    path('escala/editar/<int:pk>', EscalaEditar, name='Editar Escala'),
    path('escala/eliminar/<int:pk>', EscalaBorrar, name='Eliminar Escala'),

    path('departamento/', DepartamentoLista, name='Lista Departamento'),
    path('departamento/crear', DepartamentoCrear, name='Crear Departamento'),
    path('departamento/editar/<int:pk>', DepartamentoEditar, name='Editar Departamento'),
    path('departamento/eliminar/<int:pk>', DepartamentoBorrar, name='Eliminar Departamento'),

    path('cargo/', CargoLista, name='Lista Cargo'),
    path('cargo/crear', CargoCrear, name='Crear Cargo'),
    path('cargo/editar/<int:pk>', CargoEditar, name='Editar Cargo'),
    path('cargo/eliminar/<int:pk>', CargoBorrar, name='Eliminar Cargo'),

    path('rac/', RacLista, name='Lista Rac'),
    path('rac/crear', RacCrear, name='Crear Rac'),
    path('rac/editar/<int:pk>', RacEditar, name='Editar Rac'),
    path('rac/eliminar/<int:pk>', RacBorrar, name='Eliminar Rac'),

    path('empleado/', EmpleadoLista, name='Lista Empleado'),
    path('empleado/crear', EmpleadoCrear, name='Crear Empleado'),
    path('empleado/editar/<int:pk>', EmpleadoEditar, name='Editar Empleado'),
    path('empleado/eliminar/<int:pk>', EmpleadoBorrar, name='Eliminar Empleado'),
    path('empleado/ver/<int:pk>', EmpleadoVer, name='Ver Empleado'),

    path('variable/', VariableLista, name='Lista Variable'),
    path('variable/crear', VariableCrear, name='Crear Variable'),
    path('variable/editar/<int:pk>', VariableEditar, name='Editar Variable'),
    path('variable/eliminar/<int:pk>', VariableBorrar, name='Eliminar Variable'),

    path('formulacion/', FormulacionLista, name='Lista Formulacion'),
    path('formulacion/crear', FormulacionCrear, name='Crear Formulacion'),
    path('formulacion/editar/<int:pk>', FormulacionEditar, name='Editar Formulacion'),
    path('formulacion/eliminar/<int:pk>', FormulacionBorrar, name='Eliminar Formulacion'),

    path('elementopago/', ElementoPagoLista, name='Lista ElementoPago'),
    path('elementopago/crear', ElementoPagoCrear, name='Crear ElementoPago'),
    path('elementopago/editar/<int:pk>', ElementoPagoEditar, name='Editar ElementoPago'),
    path('elementopago/eliminar/<int:pk>', ElementoPagoBorrar, name='Eliminar ElementoPago'),

    path('pagoempleado/', PagoEmpleadoLista, name='Lista PagoEmpleado'),
    path('pagoempleado/crear', PagoEmpleadoCrear, name='Crear PagoEmpleado'),
    path('pagoempleado/editar/<int:pk>', PagoEmpleadoEditar, name='Editar PagoEmpleado'),
    path('pagoempleado/eliminar/<int:pk>', PagoEmpleadoBorrar, name='Eliminar PagoEmpleado'),


    path('prenomina/', PrenominaLista, name='Lista Prenomina'),
    path('prenomina/crear', PrenominaCrear, name='Crear Prenomina'),
    path('prenomina/editar/<int:pk>', PrenominaEditar, name='Editar Prenomina'),
    path('prenomina/eliminar/<int:pk>', PrenominaBorrar, name='Eliminar Prenomina'),
    path('prenomina/ver/<int:pk>', PrenominaVer, name='Ver Prenomina'),
    path('prenomina/ver/<int:pk>/empleado/<int:empleado>', EmpleadoPrenominaVer, name='Ver Prenomina Empleado'),

    path('nomina/', NominaLista, name='Lista Nomina'),
    path('nomina/crear', NominaCrear, name='Crear Nomina'),
    path('nomina/ver/<int:pk>', NominaVer, name='Ver Nomina'),
    path('nomina/ver/<int:pk>/empleado/<int:empleado>', EmpleadoNominaVer, name='Ver Nomina Empleado'),

    path('render/<int:pk>/',Pdf.as_view(), name='Pdf Todos'),
    path('render-nomina/<int:pk>/',PdfNomina.as_view(), name='Pdf Nomina'),

    path('empleado/<int:pk>/familia', FamiliaEmpleadoVer, name='Familia Empleado'),
    path('empleado/<int:pk>/educacion', EducacionEmpleadoVer, name='Educacion Empleado'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Nomina"
admin.site.site_title = "Nomina y Personal"
admin.site.index_title = "Bienvenido al Sistema de Nomina y Pagos"

