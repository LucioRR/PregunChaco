# Generated by Django 3.2.6 on 2021-08-24 14:16

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='imagen',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='D:\\Desarrollo\\Python\\Informatorio\\PregunChaco\\media'), upload_to=''),
        ),
    ]
