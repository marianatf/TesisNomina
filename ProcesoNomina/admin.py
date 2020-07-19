# from django.contrib import admin
# from django.db.models import Count, Sum
# from django.db.models.functions import Trunc
# from django.db.models import DateField
# #from import_export.admin import ImportExportModelAdmin
# #from import_export import resources
# # Register your models here.
# from .models import Prenomina, Nomina, PrenominaSummary
# #from import_export import resources
# from django.db.models import Q
#
#
# class InputFilter(admin.SimpleListFilter):
#     template = 'admin/input_filter.html'
#
#     def lookups(self, request, model_admin):
#         # Dummy, required to show the filter.
#         return ((),)
#
#     def choices(self, changelist):
#         # Grab only the "all" option.
#         all_choice = next(super().choices(changelist))
#         all_choice['query_parts'] = (
#             (k, v)
#             for k, v in changelist.get_filters_params().items()
#             if k != self.parameter_name
#         )
#         yield all_choice
#
#
# class CodFilter(InputFilter):
#     parameter_name = 'pagos_empleados__cod_empleado'
#     title = ('Codigo Empleado')
#
#     def queryset(self, request, queryset):
#         term = self.value()
#         if term is None:
#             return
#         any_name = Q()
#         for bit in term.split():
#             any_name &= (
#                 Q(pagos_empleados__cod_empleado=bit)  # __icontains
#             )
#         return queryset.filter(any_name)
#
#
# class NombreFilter(InputFilter):
#     parameter_name = 'pagos_empleados__cod_empleado__nombre_1'
#     title = ('Nombre Empleados')
#
#     def queryset(self, request, queryset):
#         term = self.value()
#         if term is None:
#             return
#         any_name = Q()
#         for bit in term.split():
#             any_name &= (
#                     Q(pagos_empleados__cod_empleado__nombre_1=bit) |
#                     Q(pagos_empleados__cod_empleado__apellido_1=bit)
#                 # __icontains
#             )
#         return queryset.filter(any_name)
#
#
# class DepFilter(InputFilter):
#     parameter_name = 'pagos_empleados__cod_empleado__cod_departamento__descripcion'
#     title = ('Departamento')
#
#     def queryset(self, request, queryset):
#         term = self.value()
#         if term is None:
#             return
#         any_name = Q()
#         for bit in term.split():
#             any_name &= (
#                 Q(pagos_empleados__cod_empleado__cod_departamento__descripcion=bit)  # __icontains
#             )
#         return queryset.filter(any_name)
#
#
# @admin.register(Prenomina)
# class PrenominaAdmin(admin.ModelAdmin):
#     filter_horizontal = ('pagos_empleados',)
#     list_display = ('cod_prenomina', 'tipo', 'descripcion', 'fecha_final', 'cantidad_de_pagos')
#
#     # actions = None
#     def get_readonly_fields(self, request, obj=None):
#         try:
#             if obj.editar is False:
#                 return ['pagos_empleados', 'tipo', 'descripcion', 'fecha_inicio', 'fecha_final', 'editar']
#             return []
#         except:
#             return []
#
#     def cantidad_de_pagos(self, obj):
#         return obj.pagos_empleados.count()
#
#
# @admin.register(PrenominaSummary)
# class PrenominaSummaryAdmin(admin.ModelAdmin):
#     change_list_template = 'admin/prenomina_summary_change_list.html'
#     actions = ['hola']
#     date_hierarchy = 'fecha_final'
#     list_filter = [CodFilter, NombreFilter, DepFilter, 'tipo', 'pagos_empleados__elemento_pago__codigo_ad']
#
#     #   resources_class = PrenominaSummaryResource
#     def hola(self, request, queryset):
#         queryset.update(editar=False)
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
#             'total': Count('pagos_empleados'),
#             'total_sales': Sum('pagos_empleados__monto'),
#             # 'total_sales2': Sum('pagos_empleados__monto'),
#         }
#
#         response.context_data['summary'] = list(
#             qs.values('pagos_empleados', 'pagos_empleados__cod_empleado__nombre_1',
#                       'pagos_empleados__cod_empleado__apellido_1',
#                       'pagos_empleados__monto',
#                       'pagos_empleados__elemento_pago__descripcion',
#                       'pagos_empleados__elemento_pago__codigo_ad')
#                 .annotate(**metrics)
#                 .order_by('-pagos_empleados__cod_empleado'),
#             # qs.values('pagos_empleados__cod_empleado').annotate(**metrics2).order_by('-pagos_empleados__cod_empleado')
#         )
#
#         response.context_data['summary_total'] = dict(
#             qs.aggregate(**metrics)
#         )
#
#         # summary_over_time = qs.annotate(
#         #     period=Trunc(
#         #         'fecha_final',
#         #         'day',
#         #         output_field=DateField(),
#         #     ),
#         # ).values('fecha_final').annotate(total=Sum('pagos_empleados__monto')).order_by('fecha_final')
#
#         # summary_range = summary_over_time.aggregate(
#         #     low=min('total',),
#         #     high=max('total',),
#         # )
#         # high = summary_range.get('high', 0)
#         # low = summary_range.get('low', 0)
#
#         # response.context_data['summary_over_time'] = [{
#         #     'fecha_final': x['fecha_final'],
#         #     'total': x['total'] or 0,
#         #     'pct': \
#         #        ((x['total'] or 0) - low) / (high - low) * 100
#         #        if high > low else 0,
#         # } for x in summary_over_time]
#
#         return response
#
#
# @admin.register(Nomina)
# class NominaAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(PrenominaSummary, PrenominaSummaryAdmin)