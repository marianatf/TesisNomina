# Generated by Django 2.2 on 2020-07-31 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RecursosHumanos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElementoPago',
            fields=[
                ('codigo_elemento_pago', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('descripcion', models.CharField(max_length=20)),
                ('codigo_ad', models.CharField(choices=[('asignacion', 'Asignación'), ('deduccion', 'Deducción')], default='asignacion', max_length=30, verbose_name='Asignacion/Deduccion')),
                ('frecuencia', models.CharField(blank=True, choices=[('td', 'Todas las Quincenas'), ('fm', 'Fin de Mes')], default='td', max_length=30, null=True)),
                ('codigo_fv', models.CharField(blank=True, choices=[('fijo', 'Fijo'), ('variable', 'Variable'), ('fijoingreso', 'Fijo De Ingreso')], default='variable', max_length=30, null=True)),
                ('control', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Elemento de Pago',
                'verbose_name_plural': 'Elementos de Pago',
                'db_table': 'concepto_pago',
            },
        ),
        migrations.CreateModel(
            name='Formulacion',
            fields=[
                ('codigo_formula', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('formula', models.CharField(max_length=250)),
                ('descripcion', models.CharField(default='', max_length=250)),
            ],
            options={
                'verbose_name': 'Formulacion',
                'verbose_name_plural': 'Formulaciones',
            },
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('codigo_variable', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('descripcion', models.CharField(max_length=250)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'verbose_name': 'Variable',
                'verbose_name_plural': 'Variables',
                'db_table': 'variable',
            },
        ),
        migrations.CreateModel(
            name='PagoEmpleado',
            fields=[
                ('codigo_pago', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('cantidad', models.IntegerField(blank=True, default='1', null=True)),
                ('monto', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=20, null=True)),
                ('formula', models.CharField(blank=True, max_length=250, null=True, verbose_name='Formula')),
                ('codigo_empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RecursosHumanos.Empleado')),
                ('elemento_pago', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ConceptoPago.ElementoPago')),
            ],
            options={
                'verbose_name': 'Pago de Empleado',
                'verbose_name_plural': 'Pagos de los Empleados',
                'db_table': 'pago_empleado',
                'ordering': ('codigo_empleado',),
            },
        ),
        migrations.AddField(
            model_name='elementopago',
            name='codigo_formula',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ConceptoPago.Formulacion'),
        ),
        migrations.AddField(
            model_name='elementopago',
            name='empleado_pago',
            field=models.ManyToManyField(through='ConceptoPago.PagoEmpleado', to='RecursosHumanos.Empleado'),
        ),
        migrations.AddField(
            model_name='elementopago',
            name='pago',
            field=models.ManyToManyField(through='ConceptoPago.PagoEmpleado', to='ConceptoPago.ElementoPago'),
        ),
    ]
