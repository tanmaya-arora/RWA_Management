# Generated by Django 4.2.1 on 2024-01-04 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0010_delete_productstock'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'cities'},
        ),
    ]
