# Generated by Django 4.2.5 on 2023-09-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_alter_ticket_contact_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='priority',
        ),
        migrations.AddField(
            model_name='ticket',
            name='priority_name',
            field=models.CharField(choices=[('Low', 'Low'), ('Normal', 'Normal'), ('High', 'High')], default='Normal', max_length=12),
        ),
    ]