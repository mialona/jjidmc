# Generated by Django 5.1.5 on 2025-02-10 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jjiapp', '0021_alter_presentacion_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentacion',
            name='detalles',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='presentacion',
            name='autor',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
