# Generated by Django 4.2.1 on 2024-01-04 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0020_remove_historicalticket_datetime_reply_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalticket',
            name='priority',
            field=models.CharField(default='normal', max_length=12),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(default='normal', max_length=12),
        ),
    ]
