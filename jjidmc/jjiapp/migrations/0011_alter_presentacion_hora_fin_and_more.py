# Generated by Django 5.1.5 on 2025-02-06 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jjiapp', '0010_remove_presentacion_hora_presentacion_hora_fin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentacion',
            name='hora_fin',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='presentacion',
            name='hora_inicio',
            field=models.TimeField(),
        ),
    ]
