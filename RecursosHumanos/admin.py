from django.contrib import admin

from django.db.models import Count, Sum
# Register your models here.
# from .models import (
#     Empresa,
#     Persona,
#     Familia,
#     Educacion,
#     PersonaSummary,
#     Escala,
#     Departamento,
#     Cargo,
#     Rac,
#     Empleado,
#     FamiliaEmpleado,
#     EducacionEmpleado
#
# )
from .models import *
#
# @admin.register(Empresa)
# class EmpresaAdmin(admin.ModelAdmin):
#     list_display = ['cod_empresa', 'nombre', 'rif', 'ceo', 'fecha_creacion', 'emp']
#     ordering = ['nombre', ]
#
#
class FamiliaInline(admin.StackedInline):
    model = Familia
    extra = 0
    # fieldsets = (
    #     (None, {
    #         'fields': ('cedula', ('nombre_1', 'nombre_2'), ('apellido_1', 'apellido_2'), 'fecha_nacimiento')
    #     }),
    # )
#
#
class EducacionInline(admin.StackedInline):
    model = Educacion
    extra = 0
    # fieldsets = (
    #     (None, {
    #         'fields': (('titulo', 'finalizado'), ('inicio',), ('fin',), 'aptitudes')
    #     }),
    # )


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
     pass
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
     list_display = ['codigo_solicitud', 'status', 'imagen_tag']
     inlines = [EducacionInline, FamiliaInline]
#     ordering = ['status', 'cod_solicitud', ]
#     list_filter = ['status', ]
#     search_fields = ['nombre_1', 'cedula', 'cod_solicitud', 'cargo_opt']
#     inlines = [EducacionInline, FamiliaInline]
#     radio_fields = {'status': admin.HORIZONTAL}
#     fieldsets = (
#         (None, {
#             'classes': ('extrapretty', 'wide'),
#             'fields': ('status', ('imagen'), 'cod_empresa')
#         }), ('Datos Personales', {
#             'classes': ('extrapretty', 'wide'),
#             'fields': (
#             'cedula', ('nombre_1', 'nombre_2'), ('apellido_1', 'apellido_2'), 'fecha_nacimiento', ('edad', 'genero'))
#
#         }), ('Contacto', {
#             'classes': ('extrapretty', 'wide'),
#             'fields': (('email', 'telf'), 'ocupacion', 'cargo_opt')
#
#         })
#     )
#
#
# @admin.register(PersonaSummary)
# class PersonaSummaryAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/persona_summary_change_list.html'
#     actions = False
#     date_hierarchy = 'fech_ing'
#     list_filter = ('status', 'cod_empresa')
#
#     def has_add_permission(self, request, obj=None):
#         return False
#
#     def has_change_permission(self, request, obj=None):
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#     def changelist_view(self, request, extra_context=None):
#         response = super().changelist_view(
#             request,
#             extra_context=extra_context,
#         )
#
#         try:
#             qs = response.context_data['cl'].queryset
#         except (AttributeError, KeyError):
#             return response
#
#         metrics = {
#             'total': Count('cod_solicitud'),
#             'total_sales': Sum('cod_solicitud'),
#
#         }
#
#         response.context_data['summary'] = list(
#             qs
#                 .values('status')
#                 .annotate(**metrics)
#                 .order_by('-status')
#         )
#         response.context_data['summary_total'] = dict(
#             qs.aggregate(**metrics)
#         )
#
#         return response
#
#
# @admin.register(Escala)
# class EscalaAdmin(admin.ModelAdmin):
#     list_display = ['escala', 'grado', 'paso', 'sueldo', 'cod_empresa', 'porct']
#     ordering = ['escala', 'grado']
#     list_filter = ['cod_empresa', 'escala']
#     fieldsets = (
#         (None, {
#             'classes': ('extrapretty', 'wide'),
#             'fields': ('cod_empresa', 'escala', ('grado', 'paso'), ('sueldo', 'porct'))
#         }),
#     )
#
#
# @admin.register(Departamento)
# class DepartamentoAdmin(admin.ModelAdmin):
#     list_display = ['descripcion', 'cod_empresa']
#     ordering = ['cod_empresa', 'descripcion']
#     list_filter = ['cod_empresa']
#
#
# @admin.register(Cargo)
# class CargoAdmin(admin.ModelAdmin):
#     list_display = ['cargo', 'sueldo', 'cod_empresa']
#     list_filter = ['cod_empresa']
#
#
# @admin.register(Rac)
# class RacAdmin(admin.ModelAdmin):
#     list_display = ['cod_rac', 'sueldo', 'cod_cargo', 'cod_departamento', 'cod_empresa', 'ocupado']
#     list_filter = ['cod_empresa', 'ocupado']
#     raw_id_fields = ("cod_empresa",)
#
#
# class FamiliaEmpleadoInline(admin.StackedInline):
#     model = FamiliaEmpleado
#     extra = 0
#     fieldsets = (
#         (None, {
#             'fields': ('cedula', ('nombre_1', 'nombre_2'), ('apellido_1', 'apellido_2'), 'fecha_nacimiento')
#         }),
#     )
#
#
# class EducacionEmpleadoInline(admin.StackedInline):
#     model = EducacionEmpleado
#     extra = 0
#     fieldsets = (
#         (None, {
#             'fields': (('titulo', 'finalizado'), ('inicio',), ('fin',), 'aptitudes')
#         }),
#     )
#
#     class Media:
#         js = ("js/selected.js",)
#
#
# @admin.register(Empleado)
# class EmpleadoAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'cod_empresa', 'nombre_1', 'cedula', 'status', 'imagen_tag')
#     list_filter = ('status',)
#     search_fields = ('nombre_1', 'cedula')
#     inlines = (EducacionEmpleadoInline, FamiliaEmpleadoInline)
#     # list_display = ['pk','cod_empresa', 'nombre_1', 'cedula', 'apellido_1', 'status','imagen_tag']
#     # ordering = ['status',]
#     # list_filter = ['status',]
#     # search_fields = ['nombre_1', 'cedula',]
#     # inlines = [EducacionEmpleadoInline,FamiliaEmpleadoInline]
#     raw_id_fields = ("cod_empresa", 'cod_solicitud',)