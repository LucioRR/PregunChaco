# Generated by Django 3.2.6 on 2021-09-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20210828_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='imagen_perfil',
            field=models.ImageField(blank=True, default='default_profile_pic.png', null=True, upload_to='perfil/'),
        ),
    ]
