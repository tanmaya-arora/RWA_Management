# Generated by Django 4.2.5 on 2023-09-21 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0008_ticket_datetime_reply_ticket_reply_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='datetime_reply',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='reply_message',
        ),
    ]
