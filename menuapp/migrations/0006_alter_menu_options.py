# Generated by Django 4.2.1 on 2023-08-11 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0005_logger'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu', 'verbose_name_plural': 'Menu'},
        ),
    ]
