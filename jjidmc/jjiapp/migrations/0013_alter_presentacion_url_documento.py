# Generated by Django 5.1.5 on 2025-02-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jjiapp', '0012_presentacion_destacado_presentacion_url_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentacion',
            name='url_documento',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
