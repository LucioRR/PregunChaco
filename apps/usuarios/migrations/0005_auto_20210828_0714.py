# Generated by Django 3.2.6 on 2021-08-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_perfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='imagen',
        ),
        migrations.AddField(
            model_name='perfil',
            name='facebook_url',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='imagen_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='media/perfil/'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='instagram_url',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='twitter_url',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
