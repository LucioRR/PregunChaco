# Generated by Django 3.2.6 on 2021-08-31 03:12

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0007_alter_categoria_logo_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='logo_categoria',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='C:\\LUCIO\\_PregunChaco2\\media'), upload_to=''),
        ),
    ]
