# Generated by Django 4.2.1 on 2023-07-26 12:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0016_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='aniversary_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='familymember',
            name='child_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]