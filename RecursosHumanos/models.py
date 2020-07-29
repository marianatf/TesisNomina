from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import date
from django.db.models import Count
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver
from dateutil.relativedelta import relativedelta


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class Empresa(models.Model):
    codigo_empresa = models.AutoField(unique=True, primary_key=True)
    nombre = models.CharField(max_length=50, null=True, verbose_name='Nombre de la Empresa')
    rif = models.CharField(max_length=10)
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Creacion de Empresa')
    ceo = models.CharField(max_length=50, verbose_name='Fundador de la Empresa')
    cantidad_empleado = models.PositiveIntegerField(verbose_name='Cantidad de Empleados')
    proposito = models.TextField(verbose_name='Proposito de la Empresa')
    fecha_update = models.DateField(auto_now=True)


    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        db_table = 'organizacion'


class Persona(models.Model):
    codigo_solicitud = models.AutoField(primary_key=True)
    STATUS = (
        ('trabajando', 'Trabajando'),
        ('desempleado', 'Desempleado'),
    )
    GENERO = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
        ('ninguno', 'Prefiero No Decirlo'),
    )
    NACIONALIDAD = (
        ('V','V'),
        ('E','E')
    )
    status = models.CharField(blank=True, null=True, choices=STATUS, max_length=30, default='desempleado', verbose_name='Estado De La Persona')
    cedula = models.IntegerField(verbose_name='Cedula')
    apellido = models.CharField(max_length=30, verbose_name='Primer Apellido')
    nombre = models.CharField(max_length=30, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(max_length=30, verbose_name='Segundo Nombre', blank=True, null=True)
    segundo_apellido = models.CharField(max_length=30, verbose_name='Segundo Apellido', blank=True, null=True)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name="Fecha de Nacimiento")
    ocupacion_actual = models.CharField(max_length=30, verbose_name='Ocupacion Actual', blank=True, null=True)
    cargo_optar = models.CharField(max_length=30, verbose_name='Cargo a Optar', blank=True, null=True)
    email = models.EmailField(verbose_name='Email')
    telefono = models.CharField(max_length=30, verbose_name='Telefono')
    genero = models.CharField(choices=GENERO, max_length=50, null=True, blank=True)
    fecha_ingreso = models.DateField(auto_now=True)
    imagen = models.ImageField(upload_to='candidato', blank=True, null=True)
    direccion = models.TextField(blank=True, null=True, verbose_name='Direccion')
    profesion = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    municipio = models.CharField(max_length=30, blank=True, null=True)
    parroquia = models.CharField(max_length=30, blank=True, null=True)
    nacionalidad = models.CharField(max_length=30, choices=NACIONALIDAD, default='V')
    rif = models.CharField(max_length=30, blank=True, null=True)

    def year_betwen(self):
        return abs(self.fecha_ingreso - self.fecha_nacimiento)

    def imagen_tag(self):
        if self.imagen:
            return mark_safe('<img src="%s" style="width: 45px; height:45px; margin-left: 30px" />' % self.imagen.url)
        else:
            return 'No Existe'

    def __str__(self):
            return '(%s) %s %s %s %s' % (self.pk,self.nombre, self.segundo_nombre, self.apellido, self.segundo_apellido)

    def get_age(self):
        return int((date.today() - self.fecha_nacimiento).days/365.25)


    imagen_tag.short_description = 'Imagen'
    imagen_tag.allow_tags = True

    class Meta:
        verbose_name = 'Solicitud De Ingreso'
        verbose_name_plural = 'Solicitudes De Ingresos'
        db_table = 'candidato'


class Familia(models.Model):
    codigo_familia = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    cedula = models.IntegerField(blank=True, null=True, verbose_name='Cedula')
    apellido = models.CharField(max_length=30, verbose_name='Primer Apellido')
    nombre = models.CharField(max_length=30, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(max_length=30, verbose_name='Segundo Nombre', blank=True, null=True)
    segundo_apellido = models.CharField(max_length=30, verbose_name='Segundo Apellido', blank=True, null=True)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,
                                        verbose_name="Fecha de Nacimiento")

    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familiares"
        db_table = 'familia__candidato'


class Educacion(models.Model):
    codigo_educacion = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, verbose_name='Titulo Obtenido')
    finalizado = models.BooleanField()
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,
                              verbose_name='Fecha De Inicio Del Curso')
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,
                           verbose_name='Fecha De Obtencion Del Titulo')
    aptitudes = models.CharField(max_length=50, verbose_name='Aptitud o Habilidad Obtenida')

    class Meta:
        verbose_name = "Nivel Educativo"
        verbose_name_plural = "Educacion"
        db_table = 'educacion__candidato'


class PersonaSummary(Persona):
    class Meta:
        proxy = True
        verbose_name = 'Informacion de Solicitud'
        verbose_name_plural = 'Informacion de Solicitudes'


class Escala(models.Model):
    ESCALA = (
        ('1', 'Escala Nivel I'),
        ('2', 'Escala Nivel II'),
        ('3', 'Escala Nivel III'),
        ('4', 'Escala Nivel IV'),
    )

    codigo_escala = models.AutoField(unique=True, primary_key=True, verbose_name='Codigo De Escala')
    escala = models.CharField(choices=ESCALA, max_length=20, verbose_name='Nombre Escala')
    grado = models.IntegerField(verbose_name='Grado')
    paso = models.IntegerField(verbose_name='Paso')
    sueldo = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Sueldo Base')

    class Meta:
        ordering = ['escala']
        unique_together = ['escala', 'grado', 'paso']
        verbose_name = "Escala de Sueldo"
        verbose_name_plural = "Escala de Sueldos"
        db_table = 'escala_sueldo'

    def __str__(self):
        return ' Escala %s | Grado %s | Paso %s | Sueldo = %s' % (self.escala, self.grado, self.paso, self.sueldo)


class Departamento(models.Model):
    codigo_departamento = models.AutoField(unique=True, primary_key=True, verbose_name='Codigo Del Departamento')
    descripcion = models.CharField(max_length=50, null=True, verbose_name='Descripcion')
    cantidad_empleado = models.IntegerField(blank=True, null=True, verbose_name='Cantidad De Empleados')
    presupuesto = models.FloatField(verbose_name='Presupuesto', blank=True, null=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['codigo_departamento','descripcion']
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        db_table = 'departamento'


class Cargo(models.Model):
    codigo_cargo = models.AutoField(unique=True, primary_key=True, verbose_name='Codigo Del Cargo')
    cargo = models.CharField(max_length=50, null=True, verbose_name='Nombre del Cargo')
    descripcion = models.TextField(verbose_name='Descripcion del Cargo', null=True, blank=True)

    def __str__(self):
        return self.cargo

    class Meta:
        ordering = ['cargo']
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        db_table = 'cargo'


class Rac(models.Model):
    codigo_rac = models.AutoField(unique=True, primary_key=True, verbose_name='Codigo Puesto')
    codigo_departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Departamento')
    codigo_cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Cargo')
    codigo_escala = models.ForeignKey(Escala, on_delete=models.SET_NULL, blank=True, null=True)
    compensacion = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateField(auto_now=True)
    cargo_ocupado = models.BooleanField(default=False)



    def __str__(self):
        return ' (%s) %s, %s' % (self.codigo_rac, self.codigo_cargo, self.codigo_departamento)

    class Meta:
        ordering = ['codigo_rac','codigo_departamento']
        verbose_name = "Puesto de Trabajo"
        verbose_name_plural = "Puestos de Trabajos"
        db_table = 'rac'


class Empleado(models.Model):
    codigo_empleado = models.AutoField(unique=True, primary_key=True)
    STATUSE = (
        ('nuevo_ingreso', 'Nuevo Ingreso'),
        ('trabajando', 'Activo'),
    )
    GENERO = (
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
        ('ninguno', 'Prefiero No Decirlo'),
    )
    NACIONALIDAD = (
        ('V', 'V'),
        ('E', 'E')
    )
    CIVIL = (
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viudo', 'Viudo(a)'),
        ('soltero', 'Soltero(a)'),
    )
    TIPOCUENTA = (
        ('ahorro', 'Ahorro'),
        ('corriente', 'Corriente'),
    )
    FORMAPAGO = (
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia'),
        ('deposito', 'Depósito'),
        ('cheque', 'Cheque'),
    )
    cedula = models.IntegerField(blank=True, null=True, verbose_name='Cedula')
    codigo_solicitud = models.OneToOneField(Persona, blank=True, null=True, on_delete=models.SET_NULL,verbose_name='Solicitud Empleado')
    apellido = models.CharField(max_length=30,blank=True, null=True, verbose_name='Primer Apellido')
    nombre = models.CharField(max_length=30,blank=True, null=True, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(max_length=30, verbose_name='Segundo Nombre', blank=True, null=True)
    segundo_apellido = models.CharField(max_length=30, verbose_name='Segundo Apellido', blank=True, null=True)
    codigo_rac = models.OneToOneField(Rac, on_delete=models.SET_NULL, blank=True, null=True)
    sueldo = models.FloatField(verbose_name='Sueldo Empleado', blank=True, null=True)
    fecha_ingreso = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Ingreso', blank=True,null=True)
    fecha_update = models.DateField(auto_now=True)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name="Fecha de Nacimiento")
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    telefono = models.CharField(max_length=30, blank=True, null=True, verbose_name='Telefono')
    genero = models.CharField(choices=GENERO, max_length=50, null=True, blank=True)
    imagen = models.ImageField(upload_to='empleados', blank=True, null=True)
    status_trabajador = models.CharField(choices=STATUSE,blank=True, null=True, max_length=30, default='Trabajando', verbose_name='Estado De La Persona')
    direccion = models.TextField(blank=True, null=True, verbose_name='Direccion')
    profesion = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    municipio = models.CharField(max_length=30, blank=True, null=True)
    parroquia = models.CharField(max_length=30, blank=True, null=True)
    nacionalidad = models.CharField(max_length=30,blank=True, null=True, choices=NACIONALIDAD, default='V')
    rif = models.CharField(max_length=30, blank=True, null=True)
    estado_civil = models.CharField(choices=CIVIL, max_length=30, blank=True, null=True)
    forma_pago = models.CharField(choices=FORMAPAGO, max_length=30, blank=True, null=True)
    tipo_cuenta = models.CharField(choices=TIPOCUENTA, max_length=30, blank=True, null=True)
    banco = models.CharField(max_length=30, blank=True, null=True)
    cuenta = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.codigo_solicitud:
            self.cedula = self.codigo_solicitud.cedula
            self.apellido = self.codigo_solicitud.apellido
            self.nombre = self.codigo_solicitud.nombre
            self.segundo_nombre = self.codigo_solicitud.segundo_nombre
            self.segundo_apellido = self.codigo_solicitud.segundo_apellido
            self.fecha_nacimiento  = self.codigo_solicitud.fecha_nacimiento
            self.email = self.codigo_solicitud.email
            self.telefono = self.codigo_solicitud.telefono
            self.genero = self.codigo_solicitud.genero
            self.imagen = self.codigo_solicitud.imagen
            self.direccion = self.codigo_solicitud.direccion
            self.profesion = self.codigo_solicitud.profesion
            self.estado = self.codigo_solicitud.estado
            self.municipio = self.codigo_solicitud.municipio
            self.parroquia = self.codigo_solicitud.parroquia
            self.nacionalidad = self.codigo_solicitud.nacionalidad
            self.rif = self.codigo_solicitud.rif

        super(Empleado, self).save(*args, **kwargs)

    def nombre_completo(self):
        return '%s %s ' % (self.nombre, self.apellido)

    def __str__(self):
        return '(%s) %s %s' % (self.codigo_empleado, self.nombre, self.apellido)

    def get_age(self):
        if self.fecha_nacimiento:
            return int((date.today() - self.fecha_nacimiento).days/365.25)
        return None
    # def imagen_tag(self):
    #     if self.imagen:
    #         return mark_safe('<img src="%s" style="width: 45px; height:45px; margin-left: 30px" />' % self.imagen.url)
    #     else:
    #         return 'No Existe Imagen'
    #
    # imagen_tag.short_description = 'Imagen'
    # imagen_tag.allow_tags = True

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        db_table = 'empleado'


class FamiliaEmpleado(models.Model):
    codigo_familia = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cedula = models.IntegerField(blank=True, null=True, verbose_name='Cedula')
    apellido = models.CharField(max_length=30, verbose_name='Primer Apellido')
    nombre = models.CharField(max_length=30, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(max_length=30, verbose_name='Segundo Nombre', blank=True, null=True)
    segundo_apellido = models.CharField(max_length=30, verbose_name='Segundo Apellido', blank=True, null=True)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,
                                        verbose_name="Fecha de Nacimiento")

    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familiares"
        db_table = 'familia_empleado'


class EducacionEmpleado(models.Model):
    codigo_educ = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, verbose_name='Titulo Obtenido')
    finalizado = models.BooleanField()
    fecha_inicio = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,
                              verbose_name='Fecha De Inicio Del Curso')
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True,
                           verbose_name='Fecha De Obtencion Del Titulo')
    aptitudes = models.CharField(max_length=50, verbose_name='Aptitud o Habilidad Obtenida')

    class Meta:
        verbose_name = "Nivel Educativo"
        verbose_name_plural = "Educacion"
        db_table = 'educacion_empleado'


#
# def add_familia(sender, instance, *args, **kwargs):
#     if instance.persona.status == 'ingresado':
#         familiares = Familia.objects.filter(persona=instance.persona.pk)
#         empleados = Empleado.objects.get(codigo_solicitud=instance.persona.pk)
#         for familia in familiares:
#             b = FamiliaEmpleado.objects.get_or_create(
#                 persona=empleados,
#                 cedula=familia.cedula,
#                 apellido=familia.apellido,
#                 segundo_apellido=familia.segundo_apellido,
#                 nombre=familia.nombre,
#                 segundo_nombre=familia.segundo_nombre,
#                 fecha_nacimiento=familia.fecha_nacimiento)[0]
#             b.save()
#
#
# def add_educacion(sender, instance, *args, **kwargs):
#     if instance.persona.status == 'ingresado':
#         edu = Educacion.objects.filter(persona=instance.persona.pk)
#         empleados = Empleado.objects.get(codigo_solicitud=instance.persona.pk)
#         for educacion in edu:
#             b = EducacionEmpleado.objects.get_or_create(
#                 persona=empleados,
#                 titulo=educacion.titulo,
#                 finalizado=educacion.finalizado,
#                 fecha_inicio=educacion.fecha_inicio,
#                 fecha_fin=educacion.fecha_fin,
#                 aptitudes=educacion.aptitudes)[0]
#             b.save()
#
#
# def add_empleados(sender, instance, *args, **kwargs):
#     if instance.status == 'ingresado':
#         a = Empleado.objects.get_or_create(
#             cedula=instance.cedula,
#             codigo_solicitud=instance,
#             apellido=instance.apellido,
#             segundo_apellido=instance.segundo_apellido,
#             nombre=instance.nombre_1,
#             segundo_nombre=instance.segundo_nombre,
#             fecha_ingreso=instance.fecha_ingreso,
#             codigo_empresa=instance.codigo_empresa,
#             fecha_nacimiento=instance.fecha_nacimiento,
#             edad=instance.edad,
#             email=instance.email,
#             telefono=instance.telefono,
#             genero=instance.genero,
#             status_empleado='nuevo_ingreso',
#             sueldo=0,
#             imagen=instance.imagen
#         )[0]
#         a.save()
#

# def change_bool_rac(sender, instance, *args, **kwargs):
#     if instance.codigo_rac:
#         a = Rac.objects.update_or_create(pk=instance.codigo_rac.pk)[0]
#         a.ocupado = True
#         a.save()
#
#
# post_save.connect(change_bool_rac, sender=Empleado)
# post_save.connect(add_empleados, sender=Persona)
# post_save.connect(add_educacion, sender=Educacion)
# post_save.connect(add_familia, sender=Familia)

