# Generated by Django 3.2.6 on 2021-09-02 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0012_remove_perfil_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='id',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user'),
        ),
    ]
