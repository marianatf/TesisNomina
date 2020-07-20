from django.db import models
from ConceptoPago.models import PagoEmpleado
from django.db.models import Count, Sum


# Create your models here.

class Prenomina(models.Model):
    PG = (
        ('obreros', 'Obreros'),
        ('trabajadores', 'Trabajadores'),
        ('ejecutivo', 'Ejecutivo'),
    )
    codigo_prenomina = models.AutoField(unique=True, primary_key=True)
    tipo = models.CharField(choices=PG, max_length=30, default='trabajadores', verbose_name='Tipo de Nomina')
    descripcion = models.CharField(max_length=20, blank=True, null=True)
    pagos_empleados = models.ManyToManyField(PagoEmpleado)
    fecha_inicio = models.DateField(blank=True, null=True, verbose_name='Fecha Inicio Periodo')
    fecha_final = models.DateField(blank=True, null=True, verbose_name='Fecha Ejecucion')
    editar = models.BooleanField(blank=True, null=True)

    def sumatoria(self, *args, **kwargs):
        sumatoria = Prenomina.objects.filter(pk=self.codigo_prenomina).aggregate(Sum('pagos_empleados__monto'))
        return float(sumatoria['pagos_empleados__monto__sum'])

    def sumatoria_all(self):
        return Prenomina.objects.aggregate(Sum('pagos_empleados__monto'))

    def count():
        return Prenomina.objects.aggregate(Count('codigo_prenomina'))

    def countemp():
        return Prenomina.objects.filter(pagos_empleados__elemento_pago__codigo_ad='asignacion').aggregate(
            Count('pagos_empleados__cod_empleado'))

    def __str__(self):
        return '%s - %s' % (self.descripcion, self.fecha_final)

    class Meta:
         db_table = 'pre_nomina'


# ModelName.objects.filter(field_name__isnull=True).aggregate(Sum('field_name'))


class Nomina(models.Model):
    codigo_nomina = models.AutoField(unique=True, primary_key=True)
    codigo_prenomina = models.ForeignKey(Prenomina, verbose_name='Prenomina Procesada', on_delete=models.CASCADE)
    procesado = models.BooleanField(verbose_name='Procesar Nomina')

    def __str__(self):
        return '%s - %s' % (self.codigo_prenomina.descripcion, self.codigo_prenomina.fecha_final)
    class Meta:
        db_table = 'nomina'

class PrenominaSummary(Prenomina):
    class Meta:
        proxy = True
        verbose_name = 'Informacion Nomina'
        verbose_name_plural = 'Vista Sobre las Pre Nominas'
