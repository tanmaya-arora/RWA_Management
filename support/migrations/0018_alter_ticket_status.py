# Generated by Django 4.2.5 on 2023-10-06 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0017_remove_ticket_resolved_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('closed', 'Closed'), ('pending', 'Pending'), ('opened', 'Opened'), ('reopened', 'Re opened')], max_length=28),
        ),
    ]
