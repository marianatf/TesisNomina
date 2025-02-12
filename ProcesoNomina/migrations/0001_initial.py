# Generated by Django 2.2 on 2020-07-31 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ConceptoPago', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prenomina',
            fields=[
                ('codigo_prenomina', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha Inicio Periodo')),
                ('fecha_final', models.DateField(blank=True, null=True, verbose_name='Fecha Ejecucion')),
                ('editar', models.BooleanField(default=True)),
                ('pagos_empleados', models.ManyToManyField(to='ConceptoPago.PagoEmpleado')),
            ],
            options={
                'db_table': 'pre_nomina',
            },
        ),
        migrations.CreateModel(
            name='Nomina',
            fields=[
                ('codigo_nomina', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('procesado', models.BooleanField(verbose_name='Procesar Nomina')),
                ('codigo_prenomina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProcesoNomina.Prenomina', verbose_name='Prenomina Procesada')),
            ],
            options={
                'db_table': 'nomina',
                'ordering': ['-codigo_nomina'],
            },
        ),
        migrations.CreateModel(
            name='PrenominaSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Informacion Nomina',
                'verbose_name_plural': 'Vista Sobre las Pre Nominas',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('ProcesoNomina.prenomina',),
        ),
    ]
