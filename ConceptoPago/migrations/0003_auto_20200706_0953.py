# Generated by Django 2.2 on 2020-07-06 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ConceptoPago', '0002_remove_elementopago_formula'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='elementopago',
            table='concepto_pago',
        ),
        migrations.AlterModelTable(
            name='formulacion',
            table='formula',
        ),
        migrations.AlterModelTable(
            name='pagoempleado',
            table='pago_empleado',
        ),
        migrations.AlterModelTable(
            name='variable',
            table='variable',
        ),
    ]
