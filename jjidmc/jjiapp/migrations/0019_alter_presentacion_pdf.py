# Generated by Django 5.1.5 on 2025-02-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jjiapp', '0018_alter_presentacion_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentacion',
            name='pdf',
            field=models.FileField(null=True, upload_to='jjiapp/pdf'),
        ),
    ]
