# Generated by Django 5.1.5 on 2025-02-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jjiapp', '0004_edicion_remove_presentation_edition_presentacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='edicion',
            name='parners',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='edicion',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
    ]
