from django.db import models
from RecursosHumanos.models import *
from datetime import datetime
from django.contrib.auth.models import User
from dateutil.relativedelta import *

# Create your models here.
class Variable(models.Model):
    codigo_variable = models.AutoField(unique=True, primary_key=True)
    descripcion = models.CharField(max_length=250)
    monto = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return '%s ,  Monto: %s' % (self.descripcion, self.monto)

    class Meta:
        verbose_name = "Variable"
        verbose_name_plural = "Variables"
        db_table = 'variable'


class Formulacion(models.Model):
    codigo_formula = models.AutoField(unique=True, primary_key=True)
    formula = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250, default='')

    def __str__(self):
        return '%s %s ' % (self.codigo_formula, self.descripcion)

    class Meta:
        verbose_name = "Formulacion"
        verbose_name_plural = "Formulaciones"




class ElementoPago(models.Model):
    AD = (
        ('asignacion', 'Asignación'),
        ('deduccion', 'Deducción'),
        ('prestamo', 'Préstamo'),
    )
    FV = (
        ('fijo', 'Fijo'),
        ('variable', 'Variable'),
        ('fijoingreso', 'Fijo De Ingreso')
    )
    FC = (

        ('td', 'Todas las Quincenas'),
        ('fm', 'Fin de Mes'),
    )

    codigo_elemento_pago = models.AutoField(unique=True, primary_key=True)
    descripcion = models.CharField(max_length=20)
    codigo_ad = models.CharField(choices=AD, max_length=30, default='asignacion', verbose_name='Asignacion/Deduccion')
    codigo_formula = models.ForeignKey(Formulacion, on_delete=models.SET_NULL, blank=True, null=True)
    frecuencia = models.CharField(choices=FC, max_length=30, default='td', blank=True, null=True)
    codigo_fv = models.CharField(choices=FV, max_length=30, default='variable', blank=True, null=True)
    control = models.CharField(max_length=100, blank=True, null=True)
    empleado_pago = models.ManyToManyField(Empleado, through='PagoEmpleado')
    pago = models.ManyToManyField('self', through='PagoEmpleado', symmetrical=False)

    def save(self, *args, **kwargs):
        # if self.codigo_ad == 'prestamo':

        super(ElementoPago, self).save(*args, **kwargs)

    def __str__(self):
        return '%s : %s ' % (self.descripcion, self.get_codigo_ad_display())

    class Meta:
        verbose_name = "Elemento de Pago"
        verbose_name_plural = "Elementos de Pago"
        db_table = 'concepto_pago'


class PagoEmpleado(models.Model):
    codigo_pago = models.AutoField(unique=True, primary_key=True)
    codigo_empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, blank=True, null=True)
    elemento_pago = models.ForeignKey(ElementoPago, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True, default='1')
    monto = models.DecimalField(decimal_places=2, max_digits=20, default='0', blank=True, null=True)
    formula = models.CharField(max_length=250, blank=True, null=True, verbose_name='Formula')

    def save(self, *args, **kwargs):
        if self.elemento_pago:
            if self.elemento_pago.codigo_formula:
                self.formula = self.elemento_pago.codigo_formula.formula
                self.formula = self.formula.replace("(sueldo)", "(self.codigo_empleado.codigo_rac.codigo_escala.sueldo)")
                self.formula = self.formula.replace("(años-servicio)",
                                                    "(relativedelta.relativedelta(datetime.now(),self.codigo_empleado.fecha_ingreso)).years")
                self.monto = eval(self.formula)
                self.formula = self.formula.replace("(self.codigo_empleado.codigo_rac.codigo_escala.sueldo)", "(sueldo)")
                self.formula = self.formula.replace(
                    "(relativedelta.relativedelta(datetime.now(),self.self.codigo_empleado.fecha_ingreso)).years",
                    "(años-servicio)")
            # else:
            #     self.monto = self.elemento_pago.codigo_formula.formula
            # if self.elemento_pago.codigo_ad == 'deduccion':
            #     self.monto = self.monto * -1
            # if self.cantidad > 0:
            #     self.monto = self.monto * self.cantidad
        # if self.elemento_pago.codigo_ad == 'prestamo':

        super(PagoEmpleado, self).save(*args, **kwargs)

    class Meta:
        ordering = ('codigo_empleado',)
        verbose_name = "Pago de Empleado"
        verbose_name_plural = "Pagos de los Empleados"
        db_table = 'pago_empleado'

    def __str__(self):
        if self.elemento_pago:
            codigo_ad = self.elemento_pago.codigo_ad
            codigo_fv = self.elemento_pago.codigo_fv
            descripcion = self.elemento_pago.descripcion
        else:
            codigo_ad = None
            codigo_fv = None
            descripcion = None

        return 'Empleado: %s, %s , %s, %s ->  %s' % (
        self.codigo_empleado, codigo_ad, codigo_fv, descripcion, self.monto)


