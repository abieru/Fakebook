# Generated by Django 2.2.5 on 2019-11-26 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created'], 'verbose_name': 'Publicación', 'verbose_name_plural': 'publicaciones'},
        ),
    ]
