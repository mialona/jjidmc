# Generated by Django 5.1.5 on 2025-02-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jjiapp', '0007_alter_presentacion_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentacion',
            name='hora',
            field=models.TimeField(null=True),
        ),
    ]
