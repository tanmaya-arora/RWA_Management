# Generated by Django 4.2.5 on 2023-09-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0007_alter_ticket_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='datetime_reply',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='reply_message',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]