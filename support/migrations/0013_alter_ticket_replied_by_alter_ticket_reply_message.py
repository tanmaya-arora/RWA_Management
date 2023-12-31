# Generated by Django 4.2.1 on 2023-09-25 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('support', '0012_alter_ticket_replied_by_delete_ticketreply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='replied_by',
            field=models.ForeignKey(default='secretary', null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='reply_message',
            field=models.TextField(null=True),
        ),
    ]
