# Generated by Django 4.2.5 on 2023-09-26 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('support', '0013_alter_ticket_replied_by_alter_ticket_reply_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='replied_by',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
    ]
