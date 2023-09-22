# Generated by Django 4.2.5 on 2023-09-22 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0010_alter_ticket_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='datetime_reply',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='replied_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='reply_message',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
