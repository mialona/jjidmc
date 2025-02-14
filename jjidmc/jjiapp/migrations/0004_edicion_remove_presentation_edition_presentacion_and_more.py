# Generated by Django 5.1.5 on 2025-02-06 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jjiapp', '0003_presentation_edition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=4)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='presentation',
            name='edition',
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('edicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jjiapp.edicion')),
            ],
        ),
        migrations.DeleteModel(
            name='Edition',
        ),
        migrations.DeleteModel(
            name='Presentation',
        ),
    ]
