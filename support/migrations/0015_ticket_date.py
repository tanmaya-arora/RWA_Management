# Generated by Django 4.2.5 on 2023-09-29 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0014_alter_ticket_replied_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
