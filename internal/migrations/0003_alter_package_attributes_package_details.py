# Generated by Django 4.2.5 on 2023-09-26 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0002_rename_payment_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_attributes',
            name='package_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internal.package_category'),
        ),
    ]
