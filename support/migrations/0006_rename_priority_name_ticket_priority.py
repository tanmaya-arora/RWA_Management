# Generated by Django 4.2.5 on 2023-09-21 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_delete_ticketpriority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='priority_name',
            new_name='priority',
        ),
    ]