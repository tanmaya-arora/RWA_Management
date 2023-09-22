# Generated by Django 4.2.5 on 2023-09-22 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('support', '0011_ticket_datetime_reply_ticket_replied_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='replied_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
        migrations.DeleteModel(
            name='TicketReply',
        ),
    ]
